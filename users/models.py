from django.db import models
from django.contrib.auth.models import AbstractUser

import materials.models


# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField()
    city = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]


class Payment(models.Model):
    METHOD_CHOICES = (
        ('Cash', 'Наличные'),
        ('Transfer to account', 'Перевод на счет'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_pay = models.DateField(auto_now_add=True)
    payment_course = models.ForeignKey(materials.models.Course, on_delete=models.CASCADE, nullable=True)
    payment_lesson = models.ForeignKey(materials.models.Lesson, on_delete=models.CASCADE, nullable=True)
    sum = models.PositiveIntegerField()
    method_payment = models.CharField(max_length=50, choices=METHOD_CHOICES)

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
