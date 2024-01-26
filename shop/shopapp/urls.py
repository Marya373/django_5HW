from django.urls import path
from shopapp.views import get_all_list_order, get_list_products_by_customer, hello, page_not_found, form_for_load_image_for_product

app_name = 'shopapp'

urlpatterns = [
    path('get_all_list_order/<name_client>/', get_all_list_order, name='get_all_list_order'),
    path('get_list_products_by_customer/<name_client>/', get_list_products_by_customer, name='get_list_products_by_customer'),
    path('hello/', hello, name='hello'),
    path('page_not_found', page_not_found, name='page_not_found'),
    path('upload/', form_for_load_image_for_product, name='form_for_load_image_for_product'),
]
