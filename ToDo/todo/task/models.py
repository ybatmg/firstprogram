from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=255)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #Relationship
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ManyToManyField(Categories)

    def __str__(self):
        return self.name

