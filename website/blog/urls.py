from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.showform),
    path('register/',views.register,name='register'),
]
