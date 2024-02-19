from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    image_url = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    views = models.IntegerField(default=0,null=False)
    likes = models.IntegerField(default=0,null=False)
    comments = models.IntegerField(default=0)
    slug = models.SlugField(unique=True,null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title+str(self.created_date))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"id:{self.id} Image:{self.image_url} Date:{self.created_date} Title:{self.title} Views:{self.views} Likes:{self.likes} Comments: {self.comments}"
    
