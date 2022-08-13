"""
from django.db import models

class  Orders:
	seller = models.CharField(max_length=255, null=False, blank=False)
	buyer = models.CharField(max_length=255, null=False, blank=False)
	item = models.CharField(max_length=255, null=False, blank=False)
	transaction = models.UUIDField(max_length=255, null=False, blank=False)
	created = models.DateField(max_length=255, null=False, blank=False)
	updated = models.DateField(max_length=255, null=False, blank=False)

	class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class Transaction:
	seller = models.CharField(max_length=255, null=False, blank=False)
	buyer = models.CharField(max_length=255, null=False, blank=False)
	item = models.CharField(max_length=255, null=False, blank=False)
	transaction = models.IntergerField( null=False, blank=False)
	created = models.DateField(max_length=255, null=False, blank=False)
	updated = models.DateField(max_length=255, null=False, blank=False)

	class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

class DeliveryAddress:
	name = models.CharField(max_length=255, null=False, blank=False)
	seller = models.CharField(max_length=255, null=False, blank=False)
	buyer = models.CharField(max_length=255, null=False, blank=False)
	item = models.CharField(max_length=255, null=False, blank=False)
	transaction = models.UUIDField(max_length=255, null=False, blank=False)
	created = models.DateField(max_length=255, null=False, blank=False)
	updated = models.DateField(max_length=255, null=False, blank=False)
	user = models.ForeignKey(UserAccount, on_delete=CASCADE)

	class Meta:
        verbose_name_plural = 'Delivery Addresses'
        ordering = ['name']

    def __str__(self):
        return self.title

class DeliveryPeriod(models.Model):
    title = models.CharField(max_length=255, default=0, null=False)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Delivery Periods'
        ordering = ['slug']

    def __str__(self):
        return self.title
"""