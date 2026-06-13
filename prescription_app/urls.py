from django.urls import path
from .import views

urlpatterns = [
    
    path ('prescription-page/', views.start_prescription, name = "prescription-page"),
    
    
    
    ]