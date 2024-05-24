from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    category = models.TextField(null=True,blank=True)
    question = models.TextField(null=True,blank=True)
    option_1 = models.TextField(null=True,blank=True)
    option_2 = models.TextField(null=True,blank=True)
    option_3 = models.TextField(null=True,blank=True)
    option_4 = models.TextField(null=True,blank=True)
    correct_answer = models.TextField(null=True,blank=True)
    solution = models.TextField(null=True,blank=True)
