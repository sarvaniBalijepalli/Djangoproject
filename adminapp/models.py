from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

from django.db import models
class StudentList(models.Model):
    Register_Number=models.CharField(max_length=20,unique=True)
    Name=models.CharField(max_length=100)
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def str(self):
        return self.Register_Number

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=250)
    Feedback = models.CharField(max_length=160)

    def str(self):
        return f"{self.name} {self.email} {self.Feedback}"