from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.views.decorators.cache import cache_page    # Для кэширование файлов

urlpatterns = [
    # path('sss/', TemplateView.as_view(template_name="cart/cart.html"), name='test'),
    # path('', cache_page(60)(views.contact), name='index'),      # Пример кэширования страницы
    path('', views.contact, name='index'),
]
