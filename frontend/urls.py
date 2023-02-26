from django.urls import path
from .views import *
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name = 'frontend'

urlpatterns = [
    path('', landing, name='landing'),
    path('homepage/', homepage, name='homepage'),
    path('login_page/', login, name='login_page'),
    path('register_page/', register, name='register_page'),
    path('edit/', edit_profile, name='edit_profile'),
    path('logout/', logout_page, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

