from django.db import models
from user.models import Account

class Class(models.Model):
    title = models.CharField(max_length=150)
    creator = models.ForeignKey(Account , on_delete=models.PROTECT)
    teachers = models.ManyToManyField(Account , related_name='teacher')
    students = models.ManyToManyField(Account , related_name='student')
    password = models.CharField(max_length=100 , min_length = 8)

# Create your models here.
