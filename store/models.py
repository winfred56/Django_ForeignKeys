from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:all_products", args=[self.slug])



class Product_relations(models.Model):
    product_image = models.ForeignKey(Product, related_name='p_image', on_delete=models.CASCADE)
    product_size = models.ForeignKey(Product, related_name='p_size', on_delete=models.CASCADE)
    product_color = models.ForeignKey(Product,related_name='p_color', on_delete=models.CASCADE)
    images =  models.ImageField(upload_to='images/')
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


