from django.urls import path
from .views import *
urlpatterns=[
    path('',CatergoryView,name='Category'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]