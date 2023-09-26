import uuid

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=120, null=False)
    owner = models.ForeignKey(User, related_name='product_owner', on_delete=models.PROTECT)
    user = models.ManyToManyField(User, through='Access')

    def __str__(self):
        return self.product_name


class Access(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_access')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_product_access')
    access = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.product_name}, {self.user.username}'
