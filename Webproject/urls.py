"""
URL configuration for Webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views

from django.urls import path , include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Subadmin_panel/', include('Subadmin.urls')),
    path('', views.Homepage, name='homepage'),
    path('header/', views.Header, name='header'),
    path('Contact-Us/', views.contactUs, name='ContactUs'),
    path('About-Us/', views.aboutUs, name='AboutUs'),
    path('Readmore/<int:service_id>/', views.Read_more, name='read_more'),
    path('send-otp/', views.send_otp_view, name='send_otp'),
    path('service/', views.services, name='Service'),
    
  

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urls.py





# For development only. In production, use a web server like Nginx to serve media files.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only serve static files when DEBUG is True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Attendance function k liye and function location RSCGHR.views.py