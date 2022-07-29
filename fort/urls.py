from django.urls import path
from .import views

urlpatterns = [
    path('', views.UserListCreateView),
    
    
    
    path('sell/', views.SellListCreateView),
    path('detail/<int:id>/', views.SellDetailUpdateDeleteView),
    
    
    path('buyer/', views.BuyerListCreateView),
    path('buyer/<int:id>/', views.BuyerDetailUpdateDeleteView),
]