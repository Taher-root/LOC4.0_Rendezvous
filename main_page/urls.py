from django.urls import path

from . import views

urlpatterns = [
    path('', views.login),
    path('after',views.after),
    path('dash',views.dash),
    path('map', views.maps),
    path('use', views.use)
    
]