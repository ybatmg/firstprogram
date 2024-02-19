from django.contrib import admin
from home.models import Blog
# Register your models here.

class blogadmin(admin.ModelAdmin):
    list_display=('created_date','title','views','likes','comments',)
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Blog,blogadmin)