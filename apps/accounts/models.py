from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.core.files import File

class AccountType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return self.title

class AccountUser(models.Model):
    account_type = models.ForeignKey(AccountType, related_name="types", on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)   
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    intro = models.CharField(max_length=255, null=True, blank=True)
    date_time_created = models.DateTimeField(auto_now_add=True)
     
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='profile/', blank=True, null=True)


    class Meta:
        ordering = ['name', 'date_time_created']

    def __str__(self):
        return self.name

    
def make_thumbnail(image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'PNG', quality=90)

    thumbnail = File(thumb_io, name=image.name)

    return thumbnail