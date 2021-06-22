from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]
