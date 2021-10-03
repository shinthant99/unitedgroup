from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class LogisticsView(TemplateView):
    template_name = 'logistics.html'

class NewYangonLionsClubView(TemplateView):
    template_name = 'new yangon lions.html'

class TradingView(TemplateView):
    template_name = 'trading.html'

class WakhemaInternationalRemittanceView(TemplateView):
    template_name = 'wakhema international remittance.html'

class WakhemaMoneyChangerView(TemplateView):
    template_name = 'wakhema money changer.html'

class YouthSocietyForEducationView(TemplateView):
    template_name = 'youth society for education.html'