from django.urls import path,include
from .views import SignUpView, ProfileUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]
