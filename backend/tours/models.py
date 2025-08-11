from django.db import models

class Tour(models.Model):
    CATEGORY_CHOICES = [
        ('mashxur', 'Mashxur'),
        ('ziyorat', 'Ziyorat'),
        ('hordiq', 'Hordiq'),
        ('davolanish', 'Davolanish'),
        ('visa', 'Visa'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mashxur')
    image = models.ImageField(upload_to='tour_images/', null=True, blank=True)  # ✅ here
    def __str__(self):
        return self.title

class AllTour(models.Model):
    CATEGORY_CHOICES = [
        ('mashxur', 'Mashxur'),
        ('ziyorat', 'Ziyorat'),
        ('hordiq', 'Hordiq'),
        ('davolanish', 'Davolanish'),
        ('visa', 'Visa'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to='tours/')

    def __str__(self):
        return self.name
    
class TourImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='tours/')

    def __str__(self):
        return self.title if self.title else "Untitled Image"

class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    payment_method = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.tour.title}"
