from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from profiles.models.booking import Booking
from user_profile.models.profile import Invoice
from user_profile.models.artist import Artist
from core.utils import send_booking_confirmation_email

@login_required
@transaction.atomic
def booking_create(request):
    bookings = Booking.objects.filter(created_by = request.user)
    artists = Artist.objects.all()
    if request.method == 'POST':
        data = request.POST
        
        vat = data.get('vat', False)
        if vat == 'on':
            vat=True
            
        tax = (21 if vat else 0)
        vat_amount = (float(data['flatfee'])*tax)/100
        
        artistname=Artist.objects.get(id=data['artist_name'])
            
        Booking.objects.create(
            created_by = request.user,
            artist_name_id=data['artist_name'],
            event_name=data['event_name'],
            event_date=data['event_date'],
            venue_name=data['venue_name'],
            start_time_performance=data['start_time_performance'],
            performance_duration_in_minutes=data['performance_duration_in_minutes'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            business_name=data['business_name'],
            phone_number=data['phone_number'],
            email_address=data['email_address'],
            flatfee=data['flatfee'],
            extra_comments=data['extra_comments'],
            vat_amount=vat_amount,
            invoice_paid=bool(data.get('invoice_paid', False))
        )
        
        Invoice.objects.create(
            created_by = request.user,
            invoice_name=f"Invoice - Live performance {artistname.artist_name} at {data['event_name']} + {data['event_date']}", 
            duedate=data['event_date'],
            artistname=Artist.objects.get(id=data['artist_name']), 
            services={0:f"Live performance {artistname.artist_name} at {data['event_name']}"}, 
            amounts={0:data['flatfee']},
            paid=bool(data.get('invoice_paid', False)),
            vat=vat
            )
        
        event_date_formatted = data['event_date']
        context = {
            "time": f"{data['start_time_performance']}",
            "duration":f"{data['performance_duration_in_minutes']}",
            "event_date":data['event_date'],
            "event_day":event_date_formatted.split('-')[-1],
            "location":f"{data['venue_name']}",
            "organizer":f"{data['venue_name']}",
            "address":f"{data['venue_name']}",
            "email":f"{data['email_address']}",
            "phone":f"{data['phone_number']}",
            "extra_comments":f"{data['extra_comments']}",
        }
        send_booking_confirmation_email(data['email_address'], 'booking/Email.html', context)
        return redirect('profiles:booking_list')
    return render(request, 'booking/booking_list.html', {'bookings': bookings, 'artists':artists})

@login_required
@transaction.atomic
def booking_update(request, pk):
    artist = Artist.objects.all()
    booking = get_object_or_404(Booking, pk=pk)
    event_date_formatted = booking.event_date.strftime("%Y-%m-%d")
    
    vat = (float(booking.vat_amount)/float(booking.flatfee))*100
    tax = False
    if vat == 21:
        tax = True
    
    if request.method == 'POST':
        data = request.POST
        
        vat = data.get('vat', False)
        if vat == 'on':
            vat=True
        tax = (21 if vat else 0)
        vat_amount = (int(data['flatfee'])*tax)/100
        
        booking.artist_name_id = data['artist_name']
        booking.event_name = data['event_name']
        booking.event_date = data['event_date']
        booking.venue_name = data['venue_name']
        booking.start_time_performance = data['start_time_performance']
        booking.performance_duration_in_minutes = data['performance_duration_in_minutes']
        booking.first_name = data['first_name']
        booking.last_name = data['last_name']
        booking.business_name = data['business_name']
        booking.phone_number = data['phone_number']
        booking.email_address = data['email_address']
        booking.flatfee = data['flatfee']
        booking.extra_comments=data['extra_comments']
        booking.vat_amount = str(vat_amount)
        booking.invoice_paid = bool(data.get('invoice_paid', False))
        booking.save()
        context = {
            "time": f"{data['start_time_performance']}",
            "duration":f"{data['performance_duration_in_minutes']}",
            "event_date":data['event_date'],
            "event_day":event_date_formatted.split('-')[-1],
            "location":f"{data['venue_name']}",
            "organizer":f"{data['venue_name']}",
            "address":f"{data['venue_name']}",
            "email":f"{data['email_address']}",
            "phone":f"{data['phone_number']}",
            "extra_comments":f"{data['extra_comments']}",
        }
        send_booking_confirmation_email(data['email_address'], 'booking/Email.html', context)
        return redirect('profiles:booking_list')
    return render(request, 'booking/booking_update.html', {'booking': booking, "artists":artist, "event_date_formatted":event_date_formatted, "tax":tax})

@login_required
@transaction.atomic
def booking_delete(request, pk):
    if request.method == 'DELETE':
        invoice = get_object_or_404(Booking, id=pk)
        invoice.delete()
        return JsonResponse({'message': 'Booking deleted successfully.'}, status=200)
    return JsonResponse({'error': 'Booking request method.'}, status=400)