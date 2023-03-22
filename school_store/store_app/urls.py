from django.urls import path
from . import views
app_name = 'store_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('form', views.form, name='form'),
    path('logout', views.logout, name='logout'),
    path('welcome', views.welcome, name='welcome'),
]