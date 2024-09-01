from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import DetailView
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm

category = Category.objects.all()


def products_list(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    model = Product.objects.filter(category=cat).select_related('category')
    context = {
        'product': model,
        'category': category,
        'menu': cat,
    }
    return render(request, 'products/catalog.html', context)


def product_detail(request, slug, product_slug=None):
    product = Product.objects.select_related('category').get(slug=product_slug)
    cat = get_object_or_404(Category, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'menu': cat,
        'category': category,
        'cart_product_form': cart_product_form
    }

    return render(request, 'products/product-detail.html', context)



