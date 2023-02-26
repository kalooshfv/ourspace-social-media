from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'backend'

urlpatterns = [
    path('posts/', PostItemViews.as_view(), name='posts'),
    path('posts/<int:id>', PostItemViews.as_view(), name='post_id'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('editprofile/', CustomUserPatchView.as_view(), name='edit_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
