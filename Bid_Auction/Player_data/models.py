from django.db import models

# Create your models here.
class Player(models.Model):
    image=models.ImageField(upload_to='player/images',default="")
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=100)
    Batting_style = models.CharField(max_length=200)
    Bowling_style = models.CharField(max_length=200)

    def __str__(self):
        return self.name