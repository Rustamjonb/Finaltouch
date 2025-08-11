from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Tour, Booking, TourImage
import json
import re

# Homepage – List all tours
def home(request):
    tours = Tour.objects.all()
    return render(request, 'index.html', {'tours': tours})

def index(request):
    images = TourImage.objects.all()
    return render(request, 'index.html', {'images': images})

# Payment page – Show selected tour
def payment_page(request):
    mode = request.GET.get('mode', 'booking')
    title = request.GET.get('title', '')
    description = request.GET.get('description', '')
    price_raw = request.GET.get('price', '')
    duration = request.GET.get('duration', '')
    tourists = request.GET.get('tourists', '')

    price_display = price_raw or ''
    pay_display = ''

    if price_raw:
        # remove currency symbols and thousand separators, keep digits and dot
        s = str(price_raw).strip()
        s = re.sub(r'[,\s]', '', s)           # remove commas/spaces
        s = re.sub(r'[^\d.]', '', s)          # remove non-digit/non-dot
        try:
            price_num = float(s) if s else None
            if price_num is not None:
                half = price_num / 2
                price_display = f"${price_num:,.2f}"
                pay_display = f"${half:,.2f}"
        except Exception:
            # keep original raw string if parsing failed
            price_display = price_raw
            pay_display = ''

    context = {
        'mode': mode,
        'title': title,
        'description': description,
        'price_display': price_display,
        'pay_display': pay_display,
        'duration': duration,
        'tourists': tourists,
    }
    return render(request, 'payment.html', context)

# API – Save booking info from frontend form
@csrf_exempt
def save_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            tour = Tour.objects.get(title=data['title'])

            Booking.objects.create(
                tour=tour,
                full_name=data['fullName'],
                phone=data['phone'],
                email=data['email'],
                payment_method=data['paymentMethod'],
                is_paid=True  
            )

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})
    return render(request, "index.html", {...})
