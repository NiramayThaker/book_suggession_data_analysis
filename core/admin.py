from django.contrib import admin
from .models import Book, SearchHistory

# Register your models here.
admin.site.register(Book)
admin.site.register(SearchHistory)
