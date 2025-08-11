from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('pay/', views.payment_page, name='payment'),
    path('api/save_order/', views.save_order, name='save_order'),
]
urlpatterns = [
    path('', views.home, name='home'),  # your homepage
    path('payment/', views.payment_page, name='payment'),  # payment page
]
urlpatterns = [
    path('', views.home, name='home'),          # your homepage
    path('payment/', views.payment_page, name='payment'),  # payment page
]