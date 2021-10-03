from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path("",views.IndexView.as_view(),name='index'),
    path("contact/", views.ContactView.as_view(), name='contact'),
    path("index/", views.IndexView.as_view(), name="index"),
    path("logistics/", views.LogisticsView.as_view(), name="logistics"),
    path("newyangonlionsclub/", views.NewYangonLionsClubView.as_view(), name="newyangonlionsclub"),
    path("trading/", views.TradingView.as_view(), name="trading"),
    path("internationalremittance/", views.WakhemaInternationalRemittanceView.as_view(), name="wakhemainternationalremittance"),
    path("changer/", views.WakhemaMoneyChangerView.as_view(), name="wakhemamoneychanger"),
    path("yse/", views.YouthSocietyForEducationView.as_view(), name="yse"),
]
