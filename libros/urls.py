from django.urls import path
from . import views

urlpatterns = [
		path('', views.index, name='index'),
        path('', views.base, name='base'),
        path('listbook/', views.listbook, name='listbook')
	]