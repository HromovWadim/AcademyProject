from django.contrib import admin

# Register your models here.
from .models import Teacher, Course, Student

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)