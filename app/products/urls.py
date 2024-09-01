from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from django.views.decorators.cache import cache_page    # Для кэширование файлов


urlpatterns = [
    path('<str:slug>/', views.products_list, name='products'),
    # path('iphone/<str:slug>/', views.ProductView.as_view(), name='product'),
    path('<slug:slug>/<slug:product_slug>/', views.product_detail, name='product')
]



