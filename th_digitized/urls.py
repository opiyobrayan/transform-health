
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('upload-partner',views.upload_partners, name='upload-partner'),
    path('partners-list',views.partners_list, name='partners-list'),
    path('workplan-list',views.workplan_list, name='workplan-list'),
    path('add-partner',views.add_partner, name='add-partner'),
  
    
    
   
]
