from django.contrib import admin
from .models import Author, Book, Publisher, Reader, Genre

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Reader)
admin.site.register(Genre)
