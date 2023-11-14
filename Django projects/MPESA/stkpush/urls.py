from . import views
from django.urls import path


urlpatterns = [
    path('pay', views.pay, name='pay'),
    path('stk', views.stk, name='stk'),
]