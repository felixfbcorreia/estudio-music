from django.contrib import admin
from django.urls import path
from appgis.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', home, name='home'),
    # add
    path('add_product/', add_product, name='add_product'),
    # details
    path('product/<str:product_id>', product, name='product'),
    # edit
    path('edit_product/', edit_product, name='edit_product'),
    # delete
    path('delete_product/<str:product_id>',
         delete_product, name='delete_product'),
]
