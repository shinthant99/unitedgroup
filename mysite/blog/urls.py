from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path("",views.AboutView.as_view(),name='index'),
    path("contact", views.ContactView.as_view(), name='contact'),
    path("index", views.IndexView.as_view(), name="index")
]
