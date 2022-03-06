from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    room=models.IntegerField(null=True)
    no_of_days=models.IntegerField()
    no_of_members=models.IntegerField()
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.fullname
    
