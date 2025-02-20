from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from Service.models import service

from django.shortcuts import render, get_object_or_404



def Homepage(request):
    
    Service = service.objects.all()
    data={
         'Service':Service,
    }

    return render (request,'homepage.html',data)


def services(request):
     
    return render (request,'header.html')

def aboutUs(request):
    Service = service.objects.all()
    context = {
        'Service':Service,
    }
    return render (request,'About us.html',context)


def Read_more(request, service_id):
    Service = service.objects.all()
    service_instance = get_object_or_404(service, pk=service_id)
    context = {
        'Service':Service,
        'service': service_instance,
    }
    return render(request, 'readmore.html', context)


    
def Header(request):
    return render (request,'header.html')


def send_otp_view(request):
    return render (request,'otp.html')


#######################################################################



  
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render


def contactUs(request):
    Service = service.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message_content = request.POST.get('message')

        print(f'Name: {name}, Email: {email}, Mobile: {mobile}, Message: {message_content}')
        try:
            subject = f'{name}'
            message = f'{message_content}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email, from_email]
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            print(e)  # For debugging purposes
            messages.error(request, 'There was an error sending your message. Please try again later.')

    context = {
        'Service':Service,
    }
    return render(request, 'contact us.html',context)




def send_otp_email(email):
    otp = get_random_string(length=6, allowed_chars='1234567890')
    subject = 'Your OTP for Webproject'
    message = f'Your OTP is: {otp}'
    from_email = 'rashmiinfo6@gmail.com'
    recipient_list = [email]
    
    send_mail(subject, message, from_email, recipient_list)
    print(f'OTP email sent to {email}. OTP: {otp}')  

    return otp

    
 

    

