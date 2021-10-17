from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
]