from django.urls import path
from . import views
from .views import volunteer_for_ngo

urlpatterns = [
    path('',views.home,name = 'home'),
    path('ngo/<str:ngo>/', views.ngo_view, name='ngo_view'),
    path('ngo/<int:ngo_id>/volunteer/', volunteer_for_ngo, name='volunteer_for_ngo'),
    path('<str:category_name>/', views.categories, name='categories'),
    path('<str:category_name>/<str:location>/', views.categories, name='categories_location'),
    path('contact_us/',views.contact_us,name='contact_us'),
]
