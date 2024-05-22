from .import views
from django.urls import path

urlpatterns= [
    path('', views.index,name = 'index'),
    path('add',views.add, name = 'add')
]