from asyncio.windows_events import NULL
from io import BytesIO
from tabnanny import verbose
from PIL import Image
from apps.accounts.models import AccountUser
from django.core.files import File
from django.db import models


class Category (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['slug']

    def __str__(self):
        return self.slug

class Policy(models.Model):
    title = models.CharField(max_length=255, null = True)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    service_terms = models.CharField(max_length=255)
    payment_terms= models.CharField(max_length=255)
    policy_author = models.ForeignKey(AccountUser, related_name="policy_author", on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Delivery Periods'
        ordering = ['slug']

    def __str__(self):
        return self.title


class DeliveryPeriod(models.Model):
    title = models.CharField(max_length=255, default=0, null=False)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Delivery Periods'
        ordering = ['slug']

    def __str__(self):
        return self.title


def make_thumbnail(image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'PNG', quality=90)

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail


class Products(models.Model):
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)
    useraccount = models.ForeignKey(AccountUser, related_name="product_user", on_delete=models.CASCADE)    
    policy = models.ForeignKey(Policy, related_name="product_policy", on_delete=models.CASCADE)
    delivery_frequency = models.ForeignKey(DeliveryPeriod, related_name="delivery_frequency", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    is_stock = models.BooleanField()
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-created']  # Descending order
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'


class Services(models.Model):
    category = models.ForeignKey(Category, related_name="services", on_delete=models.CASCADE)
    account = models.ForeignKey(AccountUser, related_name="serviceuser", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']  # Descending order
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'


