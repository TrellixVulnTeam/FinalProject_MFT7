import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class Farmer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    token = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    farmer = models.ForeignKey(Farmer, related_name='products', on_delete=models.CASCADE)
    fruit_name = models.CharField(max_length=255)
    weight = models.DecimalField(null=True, blank=True, decimal_places=0, max_digits=10)
    price = models.CharField(max_length=60)
    description = models.CharField(null=False, blank=False, max_length=1000)
    farm_lat = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=6)
    farm_lng = models.DecimalField(null=True, blank=True, max_digits=12, decimal_places=6)
    province = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id


class ProductImage(models.Model):
    image_file = models.ImageField(upload_to='images', blank=True, null=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)


@receiver(models.signals.post_delete, sender=ProductImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)


class Customer(models.Model):
    id = models.AutoField('id', primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    token = models.CharField(max_length=150, null=True)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    shop_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='requests', on_delete=models.CASCADE)
    fruit_name = models.CharField(max_length=255)
    weight = models.DecimalField(null=True, blank=True, decimal_places=0, max_digits=10)
    description = models.CharField(null=False, blank=False, max_length=1000)
    customer_lat = models.DecimalField(max_digits=12, decimal_places=6)
    customer_lng = models.DecimalField(max_digits=12, decimal_places=6)
    province = models.CharField(max_length=30, default=None)
    city = models.CharField(max_length=30, default=None)
    address = models.CharField(max_length=150, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.id

# class Location(models.Model):
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     street = models.CharField('street', max_length=30, blank=True)
#     city = models.CharField('city', max_length=30, blank=True)
#     province = models.CharField('province', max_length=30, blank=True)

# class Payment(models.Model):
#     id = models.AutoField(primary_key=True)
#     state = models.BooleanField()
#     price = models.CharField('price',max_length=30,blank=False)
#
