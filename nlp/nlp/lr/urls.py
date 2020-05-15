from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import EndpointView
from . import views
from django.urls import path
from django.conf.urls import include


router = routers.DefaultRouter()
router.register('nlp', views.EndpointView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('form/', views.houseprice, name="houseprice"),
]
