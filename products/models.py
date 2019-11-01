from django.db import models


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField("Subcategory Name", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    # name = models.CharField("Product Name")
    # brand = models.CharField("Brand", max_length=100)defs
    pass
