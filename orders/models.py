from django.conf import settings
from django.db import models
from products.models import Product

User = settings.AUTH_USER_MODEL

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.id


class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField("Quantity", default=1)

  def __str__(self):
    return self.id