from django.shortcuts import get_object_or_404, render, redirect
from NGO.models import ngos
from django.contrib.auth import login as auth_login
from Users.models import UserProfile, User, Volunteer
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from ChatApp.models import ChatRoom
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user instance and returns it
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            # Create a chat room for the new user with admin (assuming owner is admin)
            admin_user = User.objects.filter(is_superuser=True).first()  # Assuming the first superuser is the admin
            if admin_user:
                ChatRoom.objects.create(user=user, owner=admin_user)
            else:
                print("Admin user not found!")  # Debug print

            # Automatically log in the user after registration
            auth_login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def user_profile(request, user_id):
    # Fetch the UserProfile associated with the given user_id
    uprofile = get_object_or_404(UserProfile, user_id=user_id)
    # print(uprofile.image)
    volunteered_ngos = Volunteer.objects.filter(user_profile = uprofile)
    print(volunteered_ngos)
    return render(request, 'Users/userProfile.html', {'profile':uprofile, 'ngos': volunteered_ngos})
