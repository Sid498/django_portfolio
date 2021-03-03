from .models import *
from portfolio_prj import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


class HomeView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['post', 'get']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()

        return context
    @csrf_exempt
    def post(self, request,  *args, **kwargs):
        if request.method == "POST":
            message = request.POST['message']
            user_name = request.POST['name']
            user_email = request.POST['email']
            try:
                send_mail('Test Subject', message +" \nfrom "+user_name+" "+user_email, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, user_email])
            except Exception:
                print(Exception)
                return HttpResponse('Error: Invalid header found')
        return HttpResponse('Message has been sent..!!')