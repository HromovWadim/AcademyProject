from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField()
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
          verbose_name = 'Преподователь'
          verbose_name_plural = 'Преподователи'


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
         verbose_name = 'Курс'
         verbose_name_plural = 'Курсы'



class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField()
    url = models.URLField()
    date_of_birth = models.DateField()
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.first_name

    class Meta:
         verbose_name = 'Студент'
         verbose_name_plural = 'Студенты'
