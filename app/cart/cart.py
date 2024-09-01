from decimal import Decimal
from django.conf import settings
from products.models import Product


class Cart:
    def __init__(self, request):    # инициализация корзины
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        # добавить продукт в корзину или обновить его количество.

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        # обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):

        # удаление товара из корзины.

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # перебор элементов в корзине и получение продуктов из базы данных
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.select_related('category').filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

