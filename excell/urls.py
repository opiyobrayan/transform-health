
from django.urls import path
from . import views

urlpatterns = [
    path('upload-partners',views.upload_partners,name='upload-partners'),
]