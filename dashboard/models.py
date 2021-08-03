from django.db import models
from django.contrib.auth.models import User, update_last_login
# Create your models here.


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # renames the instances of the model
    # with their title name
    def __str__(self):                                  
        return self.title

    class Meta:
        verbose_name ="notes"
        verbose_name_plural = "notes"





class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length =50)
    title = models.CharField(max_length=100)
    description=models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)


    def __str__(self):                                  
        return self.title

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    def __str__(self):                                  
        return self.title




