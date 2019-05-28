from django.contrib.auth.models import User
from django.db import models


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
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Fruit(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    weight = models.DecimalField(null=True, blank=True,decimal_places=10,max_digits=10)
    price = models.DecimalField(null=False,blank=False,decimal_places=20,max_digits=20)
    description = models.CharField(null=False,blank=False,max_length=300)

    def __str__(self):
        return self.id


class FruitImage(models.Model):
    image_file = models.ImageField(upload_to='images', blank=True, null=True)
    image = models.ForeignKey(Fruit, on_delete=models.CASCADE)


class Customer(models.Model):
    id = models.AutoField('id',primary_key=True)
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
    fruit_type = models.CharField(max_length=255)
    ordered_weight = models.DecimalField(null=True, blank=True,decimal_places=10,max_digits=10)
    farmer_lat = models.DecimalField(max_digits=9, decimal_places=6)
    farmer_lng = models.DecimalField(max_digits=9, decimal_places=6)
    customer_lat = models.DecimalField(max_digits=9, decimal_places=6)
    customer_lng = models.DecimalField(max_digits=9, decimal_places=6)
    # driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)

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