# Generated by Django 4.0.4 on 2022-05-05 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['slug']},
        ),
    ]
