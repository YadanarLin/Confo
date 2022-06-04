from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model): #One class definition means a table in the database
    title=models.CharField(max_length=200, default="")
    body=models.TextField()
    like=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)