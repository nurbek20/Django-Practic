from django.db import models

# Create your models here.
class Contact(models.Model):
    last_name = models.CharField(max_length=40, verbose_name="LastName")
    first_name = models.CharField(max_length=40, verbose_name="FirstName")
    email = models.EmailField(verbose_name="Email")
    number = models.IntegerField(verbose_name="Number")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и Время")

