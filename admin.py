from django.contrib import admin
from .models import Contact,Book

class BookAdmin(admin.ModelAdmin):
    list_display=['book_name','author_name','pub_date','return_date','cost']

admin.site.register(Contact)
admin.site.register(Book,BookAdmin)