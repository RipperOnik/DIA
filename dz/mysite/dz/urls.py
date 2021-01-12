from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('k1.html', views.k1, name='k1'),
    path('k2.html', views.k2, name='k2'),
    path('g1.html', views.g1, name='g1'),
]