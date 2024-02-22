from django.urls import path
from jinjaapp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('gallery/', views.gallery, name='my_gallery')
]