import json
from django.shortcuts import get_object_or_404,render, redirect
from urllib.parse import unquote
from ChatApp.models import ChatRoom
from NGO.models import ngos
from Users.models import Volunteer
import razorpay # type: ignore
from django.contrib.auth.decorators import login_required

KEY_ID='rzp_test_djBwalTAYcz1Lr'
KEY_SECRET='dRu5ocCObLhfw74BpRbaRZoG'

def home(request):
    user = request.user
    chat_room_id = None

    if user.is_authenticated:
        chat_room = ChatRoom.objects.filter(user=user).first()
        chat_room_id = chat_room.id if chat_room else None

    context = {
        'user_chat_room_id': chat_room_id,
    }
    return render(request, 'NGO/home.html', context)

def about(request):
    return render(request,'NGO/about.html')

def contact_us(request):
    return render(request,'NGO/contact.html')

def categories(request, category_name, location=None):
    ngos_in_category = ngos.objects.filter(category=category_name)
    if location:
        ngos_in_category = ngos_in_category.filter(location=location)
    
    context = {
        'category_name': category_name,
        'location': location,
        'ngos_in_category': ngos_in_category,
    }
    return render(request, 'NGO/categories.html',context)

def ngo_view(request, ngo):
    decoded_ngo = unquote(ngo.replace("-", " "))
    ngo_reqd = get_object_or_404(ngos, name=decoded_ngo)  # Ensure exact matching

    context = {
        'ngo': ngo_reqd
    }
    return render(request, 'NGO/ngoView.html', context)

def campaigns(request):
    with open('./campaigns.json', 'r') as file:
        data = json.load(file)
    donation_drives = data.get('donation_drives', [])
    # print(donation_drives)
    context = {
        'donation_drives': donation_drives
    }
    # print(context['donation_drives'])
    return render(request,"NGO/campaigns.html",{'data':context['donation_drives']})

def donation(request):
    return render(request,"NGO/donation.html")

def payment(request,amt):
    client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
    print(amt)
    # Create an order
    response = client.order.create({
        'amount': amt*100,  # Amount in paise (change as per your requirement)
        'currency': 'INR',
        'payment_capture': 1  # Auto capture payment
    })

    order_id = response['id']
    context = {
        'order_id': order_id,
        'razorpay_api_key': KEY_ID  # Use this key in the frontend to create the payment form
    }

    return render(request,'donation.html', context)

@login_required
def volunteer_for_ngo(request, ngo_id):

    if request.method == 'POST':
        ngo = get_object_or_404(ngos, id=ngo_id)
        print(request.user)
        user_profile = request.user.userprofile  # Get the UserProfile related to the current user
        print(user_profile)
        
        # Get or create a Volunteer instance for the user_profile
        volunteer, created = Volunteer.objects.get_or_create(user_profile=user_profile)
        print(volunteer)
        # Add the NGO to the user's volunteering list if not already added
        if ngo not in volunteer.ngos_volunteering.all():
            volunteer.ngos_volunteering.add(ngo)
            volunteer.save()
        return render(request, 'NGO/success.html')
    # Redirect to some appropriate page after volunteering
    return redirect('home') 