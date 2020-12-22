from django.db import models
from django.urls import reverse

# Create your models here.


class Poll(models.Model):
    question=models.TextField()
    option_1=models.CharField(max_length=50)
    option_2=models.CharField(max_length=50)
    option_3=models.CharField(max_length=50)
    option_1_count=models.IntegerField(default=0)
    option_2_count=models.IntegerField(default=0)
    option_3_count=models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('home')