# Generated by Django 4.0.4 on 2022-05-04 00:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('vendors', '0005_vendor_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
