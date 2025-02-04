from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.hello_world, name='hello_world'),
]
