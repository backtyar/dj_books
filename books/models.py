from django.db import models
from datetime import datetime


class Book(models.Model):

    name_book = models.CharField(max_length=100, verbose_name='Название книги',unique=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE, verbose_name='Автор', related_name='author',db_index=False)
    date_publish = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    quantity_page = models.IntegerField(default=0, verbose_name='Количество страниц ')
    isbn = models.CharField(max_length=100, verbose_name='Международный стандартный книжный номер', blank=True, db_column='ISBN')

    def __str__(self):
        return self.name_book

    class Meta:
        db_table = "books"
        db_table_comment = "Question answers"
        default_permissions = ('add', 'change', 'view')
        verbose_name = 'Книги'
        verbose_name_plural = 'Книга'




class Author(models.Model):
    name_author = models.CharField(max_length=100, verbose_name='Автор', db_index=True)
    birthday = models.DateTimeField(auto_now_add=True, verbose_name="День рождение")
    country = models.CharField(max_length=100, verbose_name="Страна")

    class Meta:
        db_table = "author"
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    genre = models.CharField(max_length=100, verbose_name='Жанр', unique=True, db_column='Жанр')
    description = models.TextField(verbose_name='Описание ', db_column='Описание ')

    class Meta:
        db_table = "genre"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'




class Publisher(models.Model):
    name_Publisher = models.CharField(max_length=100, verbose_name='Название издательства')
    address = models.TextField(verbose_name='Адрес',)
    phone = models.CharField(max_length=100, verbose_name='Телефон', unique=True)



class Reader(models.Model):
    name_user = models.CharField(max_length=100, verbose_name='Название издательства')
    age = models.IntegerField(default=0, verbose_name='возрост ')


    class Meta:
        db_table = "reader"
        verbose_name = 'читатель'
        verbose_name_plural = 'читатели'
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=5), name='age_gte_5')
        ]





