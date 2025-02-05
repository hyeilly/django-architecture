from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.hello_world, name='hello_world'),
    path('api/items/', views.item_list, name='item-list'),
    path('api/items/<str:item_id>/', views.item_detail, name='item-detail'),
    path('api/articles/<int:custom_id>/', views.get_article_by_custom_id, name='article-id')
]
