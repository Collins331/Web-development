from django.urls import path
from . import views

app_name='auth'

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('signup', views.signup, name='signup'),
    path('activate/<uid>/<token>', views.activate, name='activate')
]