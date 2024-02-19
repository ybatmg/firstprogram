from django.db import models
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"name:{self.name} code:{self.code}"

class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} state:{self.state}"


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    country = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=100,blank=True,default='no title',null=True)
    rating = models.FloatField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    isBestSeller = models.BooleanField(default=False)
    published = models.DateField(auto_now=True) 
    slug = models.SlugField(unique=True,)

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title+str(self.published))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"id:{self.id} title:{self.title} rating:{self.rating}"

