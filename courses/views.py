from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import random
import string

from .models import Booking

# List of golf courses
courses = [
    {
        'id': 1,
        'name': 'Cliffside Golf Club',
        'location': 'Gallipolis, Ohio',
        'holes': 18,
        'description': 'Scenic 18-hole course along the Ohio River, open fairways, and welcoming atmosphere.',
        'image': 'cliffside.jpg',
    },
    {
        'id': 2,
        'name': 'Elks Country Club',
        'location': 'McArthur, Ohio',
        'holes': 18,
        'description': 'Wooded fairways, rolling hills, and a serene golfing environment.',
        'image': 'elks.jpg',
    },
    {
        'id': 3,
        'name': 'Franklin Valley Golf Course',
        'location': 'Jackson, Ohio',
        'holes': 18,
        'description': 'Classic Ohio course with mature trees, wide fairways, and great history.',
        'image': 'franklin.jpg',
    },
]

# Available tee times
tee_times = [
    "8:00 AM",
    "9:30 AM",
    "11:00 AM",
    "1:00 PM",
    "2:30 PM",
    "4:00 PM"
]

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        if 'guest' in request.POST:
            request.session['guest_user'] = True
            return redirect('welcome')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['guest_user'] = False
                return redirect('welcome')
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    auth_logout(request)
    return redirect('login')

# Welcome page
def welcome(request):
    return render(request, 'welcome.html', {'courses': courses})

# Home page (Explore Courses)
def home(request):
    return render(request, 'home.html', {'courses': courses})

# Course detail page
def course_detail(request, course_id):
    course = next((c for c in courses if c['id'] == course_id), None)
    return render(request, 'course_detail.html', {'course': course})

# Book tee time page
@login_required
def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course_id = int(request.POST.get('course_id'))
        tee_time = request.POST.get('tee_time')
        course = next((c for c in courses if c['id'] == course_id), None)

        confirmation_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        # Save booking into the database
        Booking.objects.create(
            user=request.user,
            course_name=course['name'],
            course_location=course['location'],
            tee_time=tee_time,
            email=email,
            phone=phone,
            confirmation_code=confirmation_code
        )

        return render(request, 'thankyou.html', {
            'name': name,
            'email': email,
            'phone': phone,
            'course': course,
            'course_image': course['image'],
            'tee_time': tee_time,
            'confirmation_code': confirmation_code
        })
    else:
        return render(request, 'book.html', {
            'courses': courses,
            'tee_times': tee_times
        })

# Thank you page
def thankyou(request):
    return render(request, 'thankyou.html')

# Profile page to show user's bookings
@login_required
def profile(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'profile.html', {'bookings': bookings})

# Cancel booking view
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.delete()
        return redirect('profile')

    return redirect('profile')












