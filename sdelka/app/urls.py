from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.index),
    path('people/<int:pk>/', PeopleDetail.as_view(), name='html-detail'),
    path('ContactForm', views.get_contact),
    # path('blog/<int:pk>/', BlogDetail.as_view(), name='css-detail'),
]
