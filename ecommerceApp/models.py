from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    desc=models.TextField(max_length=100)
    phone_no=models.IntegerField()

    def __str__(self):
        return self.name
    
