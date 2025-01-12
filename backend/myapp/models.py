from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=255)
    def __str__(self):
        return self.warehouse_name

class StaffPermission(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    manager = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    supervisor = models.BooleanField(default=False)

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Items(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='item/')
    price1 = models.PositiveIntegerField(default=0)
    price2 = models.PositiveIntegerField(default=0)
    price3 = models.PositiveIntegerField(default=0)
    price4 = models.PositiveIntegerField(default=0)
    package_unit = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ItmColor(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    color = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.color

class ItmSize(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    size = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.size


class ItemWarehouse(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    color = models.ForeignKey(ItmColor, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(ItmSize, on_delete=models.CASCADE, blank=True, null=True)
    stock_balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

