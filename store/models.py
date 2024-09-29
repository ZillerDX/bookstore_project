# store/models.py
from django.db import models
from django.contrib.auth.models import User

# หมวดหมู่ของหนังสือ
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# โมเดลข้อมูลหนังสือ
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

# โมเดลข้อมูลการสั่งซื้อ
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
