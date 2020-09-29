from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse

class Music(models.Model):
    name=models.CharField(max_length=1024,)
    image=models.CharField(max_length=1024,)
    audio=models.FileField(upload_to='media/')
    desc=models.CharField(max_length=1024,)
    date=models.DateTimeField()
    slova=models.TextField()
    category=models.CharField(max_length=1025,)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mysic_detail', args=[str(self.id)])