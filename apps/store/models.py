from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models

from apps.accounts.models import CustomUser


class Brand(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['slug']

    def __str__(self):
        return self.slug


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['slug']

    def __str__(self):
        return self.slug


class Policy(models.Model):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    service_terms = models.CharField(max_length=255)
    payment_terms = models.CharField(max_length=255)
    ordering = models.IntegerField(default=0)
    policy_author = models.ForeignKey(CustomUser, related_name="policy_author", on_delete=models.CASCADE)
    policy_category = models.ForeignKey(Category, related_name="policy_category", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Policies'
        ordering = ['slug']

    def __str__(self):
        return self.slug


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
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock_count = models.IntegerField(null=True, blank=True, default=0)
    is_active = models.BooleanField(default=True)
    review_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    product_category = models.ForeignKey(Category, related_name="product_category", default="default",
                                         on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name="brand", null=True, on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, related_name="seller", default=1, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, related_name="product_policy", default=1, on_delete=models.CASCADE)
    delivery_frequency = models.ForeignKey(DeliveryPeriod, related_name="delivery_frequency", default="default",
                                           on_delete=models.CASCADE)

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


class ProductReview(models.Model):
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, related_name="product_review", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, related_name="product_customer", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating)


class Services(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    is_active = models.BooleanField()
    service_category = models.ForeignKey(Category, related_name="service_category", on_delete=models.CASCADE)
    service_provider = models.ForeignKey(CustomUser, related_name="service_provider", on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, related_name="services_policy", default=1, on_delete=models.CASCADE)
    delivery_frequency = models.ForeignKey(DeliveryPeriod, related_name="service_delivery",
                                           default="Same Week Delivery", on_delete=models.CASCADE)

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


class ServiceReview(models.Model):
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    service = models.ForeignKey(Services, related_name="service_review", on_delete=models.CASCADE)
    createdBy = models.ForeignKey(CustomUser, related_name="service_customer", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.address)
