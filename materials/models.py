from django.db import models

# Create your models here.

class Course(models.Model):
    name_course = models.CharField(unique=True, max_length=150)
    preview = models.ImageField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name_course}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=150)
    preview = models.ImageField()
    description = models.TextField(null=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return f'{self.name_lesson}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'