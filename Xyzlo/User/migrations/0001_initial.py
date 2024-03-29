# Generated by Django 3.1.3 on 2020-12-15 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=70, verbose_name='name')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('bdate', models.DateField(verbose_name='Birthdate')),
                ('pnumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('product_image', models.ImageField(upload_to='product_images')),
                ('product_name', models.CharField(max_length=70, verbose_name='product_name')),
                ('product_price', models.IntegerField(verbose_name='product_price')),
                ('product_description', models.CharField(max_length=500, verbose_name='product_deascription')),
                ('product_category', models.CharField(max_length=70, verbose_name='product_category')),
                ('product_location', models.CharField(max_length=500, verbose_name='product_location')),
                ('pro_email', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
