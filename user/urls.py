from django.urls import path
from . import views
from .views import signin, index, signup

app_name = 'user'
urlpatterns = [
    path('', index, name='index'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),

]
