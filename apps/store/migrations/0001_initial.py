# Generated by Django 4.0.4 on 2022-08-12 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='DeliveryPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Delivery Periods',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='ProductPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('service_terms', models.CharField(max_length=255)),
                ('payment_terms', models.CharField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_policy_author', to='accounts.accountuser')),
            ],
            options={
                'verbose_name_plural': 'Delivery Periods',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('in_stock', models.BooleanField()),
                ('in_active', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('service_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_user', to='accounts.accountuser')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.category')),
                ('delivery_frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_frequency', to='products.deliveryperiod')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policy', to='products.productpolicy')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['-created'],
            },
        ),
    ]