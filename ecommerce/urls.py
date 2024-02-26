from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add',views.cart_add,name='cart_add'),
    path('register',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('product/<int:pk>',views.product,name='product'),
    path('categories/<str:victor>',views.categories,name='categories'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]