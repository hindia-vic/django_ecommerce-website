from django.urls import path
from . import views

urlpatterns=[
    path('',views.con,name='con'),
    path('add/',views.cart_add,name='cart_add'),
    path('delete',views.delete_cart,name='delete_cart'),
    path('update',views.update_cart,name='update_cart'),
]