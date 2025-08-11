from django.contrib import admin
from .models import Tour, Booking
from .models import AllTour
from django.contrib import admin
from .models import TourImage

admin.site.register(TourImage)
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration_days', 'category')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'tour', 'phone', 'payment_method', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'payment_method']
    search_fields = ['full_name', 'phone', 'tour__title']

@admin.register(AllTour)
class AllTourAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)