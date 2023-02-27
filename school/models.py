from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Фамилия, Имя')
    category = models.ForeignKey(to=Category, verbose_name='Должность', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение')

class Gallery(models.Model):
    img = models.ImageField(verbose_name='Изображение')

class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')
    category = models.ForeignKey(to=Category, verbose_name='Должность', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение')

class Graduate(models.Model):
    name = models.CharField(max_length=255, verbose_name='Фамилия Имя Отчество')
    category = models.ForeignKey(to=Category, verbose_name='Должность', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение')

class Date(models.Model):
    start = models.DateField()
    duration = models.DateField()
    end = models.DateField()

