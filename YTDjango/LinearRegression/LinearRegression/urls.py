from django.contrib import admin
from django.urls import path, include
from myApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApi.urls')),
]
