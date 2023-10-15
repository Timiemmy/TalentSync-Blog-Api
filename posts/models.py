from django.db import models
from accounts.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title