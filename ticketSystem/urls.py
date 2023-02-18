from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('signup' , views.signup , name="signup" ),
    path('showAll' , views.showAll , name="showAll" ),
    path('addBus' , views.addBus , name="addBus" ),
    path('showBuses' , views.showBuses , name="showBuses" ),
]