from django.db import models
from django.utils import timezone
# Create your models here.

class Video(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField()
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=254)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name :{}, ID:{}'.format(self.title,self.id)
