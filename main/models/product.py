from django.db import models

class ProductImages(models.Model):
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'


class Category(models.Model):
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name_uz

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_image/')
    volume = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name_uz

