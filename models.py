from io import BytesIO
from tabnanny import verbose
from PIL import Image
from apps.accounts.models import AccountUser
from django.core.files import File
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['slug']

    def __str__(self):
        return self.slug


def make_thumbnail(image, size=(400, 400)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'PNG', quality=80)

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail


