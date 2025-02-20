from django.shortcuts import render
from .models import Subadmin_user
from Service.models import service
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ServiceForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiceForm


########################################### LOGIN METHOD  START ##########################

def Sub_adminlogin(request):
    if 'user_id' in request.session:
            return redirect('/Subadmin_panel/dashboard/')
  
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            print('Email or password not provided')
            return render(request, 'Subadmin_login.html', {'error': 'Please enter both email and password'})
        
        try:
            user = Subadmin_user.objects.get(user_email=email)
            print(f'User found: {user.user_email}')
            
            if user.user_password == password:
                print('Password matched')
                request.session['user_id'] = str(user.user_id)
                return redirect('/Subadmin_panel/dashboard/')
            else:
                print('Invalid password')
                return render(request, 'Subadmin_login.html', {'error': 'Invalid password'})
        
        except Subadmin_user.DoesNotExist:
            print('User does not exist')
            return render(request, 'Subadmin_login.html', {'error': 'Invalid email'})

    return render(request, 'Subadmin_login.html')

########################################### LOGIN METHOD  CLODE ##############

################################# DASHBOARD ##################################

def Dashboard(request):
    try:
        admin_id = request.session.get('user_id')
        admin = Subadmin_user.objects.get(user_id=admin_id)
        return render (request,'Subadmin_dashboard.html')
    except Subadmin_user.DoesNotExist:
        return redirect('/Subadmin_panel/?message=Please login')

################################# ADD SERVICES ###################################

@csrf_exempt
def add_services(request):
    try:
          
        admin_id = request.session.get('user_id')
        admin = Subadmin_user.objects.get(user_id=admin_id)
  
   

        if request.method == 'POST':
            form = ServiceForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/Subadmin_panel/dashboard/')  # Redirect to the admin dashboard
        else:
            form = ServiceForm()

        return render(request, 'Subadmin_Addcards.html', {'ServiceForm': form})
    

    except Subadmin_user.DoesNotExist:
        return redirect('/Subadmin_panel/?message=Please login')

################################# ALL SERVICES ###################################
def services_list(request):
    try:
          
        admin_id = request.session.get('user_id')
        admin = Subadmin_user.objects.get(user_id=admin_id)
        all_service = service.objects.all() 
        return render(request,'Subadmin_Allservice.html', {'all_service': all_service})
    except Subadmin_user.DoesNotExist:
        return redirect('/Subadmin_panel/?message=Please login')




################################ EDIT FUNCTION ####################################

def edit_services(request):
    try:
        admin_id = request.session.get('user_id')
        admin = Subadmin_user.objects.get(user_id=admin_id)
        service_id = request.GET.get('idd')
        service_instance = get_object_or_404(service, id=service_id)

        if request.method == 'POST':
            form = ServiceForm(request.POST, request.FILES, instance=service_instance)
            if form.is_valid():
                form.save()
                return redirect('/Subadmin_panel/dashboard/') 
        else:
            form = ServiceForm(instance=service_instance)
        
        return render(request, 'Subadmin_editservice.html', {'form': form, 'service': service_instance})
    except Subadmin_user.DoesNotExist:
        return redirect('/Subadmin_panel/?message=Please login')


