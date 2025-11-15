from django.shortcuts import render, redirect
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        if name and email and phone and date and time:
            booking = Booking.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time
            )
            # Send initial email
            send_mail(
                'Booking Received',
                'Your booking is being processed. You will receive a confirmation shortly.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('home')
    return render(request, 'bookings/home.html')