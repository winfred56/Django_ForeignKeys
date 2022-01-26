from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product:all_products", args=[self.id])



class Product_relations(models.Model):
    product_image = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_color = models.ForeignKey(Product, on_delete=models.CASCADE)
    images =  models.ImageField(upload_to='images/')
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


