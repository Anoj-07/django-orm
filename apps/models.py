from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Branch(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="branches"
    )
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    selling_price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)


class Customer(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="customers"
    )
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, related_name="sales")
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name="sales"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="sales")

    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    sold_at = models.DateTimeField(auto_now_add=True)
