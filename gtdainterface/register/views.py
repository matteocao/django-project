
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm
#from django.core.mail import send_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #print('Welcome %s! \nYou are now registered. \n' % request.POST['username'])
        if form.is_valid():
            print("Form is valid")
            form.save()
            message = Mail(
                from_email='matteocao@gmail.com',
                to_emails=request.POST['email'],
                subject='Subscription Confirmation',
                plain_text_content='Welcome %s! \n You are now registered. \n' % request.POST['username'])
            
            # need to set the environment variable with `export SENDGRID_API_KEY = 'xxxxxxx'`
            #print("SMTP API key: ", settings.SENDGRID_API_KEY)
            sg =  SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

            #send_mail('Subscription Confirmation', 'Welcome %s! \n You are now registered. \n' % request.POST['username'], 'matteocao@gmail.com', [request.POST['email']], fail_silently=False)
            return redirect("/accounts/login/")
        return redirect("/register/failed/")
    else: # we go in here when we reach the regstration page
        #print("Just display the registration page.")
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})

def failedRegistration(request):
    return render(request,"register/failedRegistration.html")
