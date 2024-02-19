from django.contrib import admin
from books.models import Book,Author,Address,Country

# Register your models here.


class Bookadmin(admin.ModelAdmin):
    list_display=('title','author','price')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','author')
    list_filter = ('author','rating')


admin.site.register(Book,Bookadmin)

class Authoradmin(admin.ModelAdmin):
    list_display=('name','age','address','genre')
    search_fields = ('name','genre')
    list_filter = ('name','genre')

admin.site.register(Author,Authoradmin)

class Addressadmin(admin.ModelAdmin):
    list_display=('city','state')

admin.site.register(Address,Addressadmin)

class Countryadmin(admin.ModelAdmin):
    list_display=('name','code')

admin.site.register(Country,Countryadmin)