from django.contrib import admin
from django.urls import include, path
from NGO import views
from Users import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register,name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name='Users/login.html'),name='login'),
    path('logout/',users_views.logout_view, name='logout'),
    path('about/',views.about,name='about'),
    path('UserProfile/<int:user_id>',users_views.user_profile,name='user_profile'),
    path('campaigns/',views.campaigns,name='campaigns'),
    path('donation/',views.donation,name="donation"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path('',include('ChatApp.urls')),
    path('',include('NGO.urls')),
]
