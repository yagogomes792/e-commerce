from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class ProducQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)
    
    def featured(self):
        return self.filter(featured = True, active = True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProducQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(blank= True, unique = True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()
    
    def __str__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)