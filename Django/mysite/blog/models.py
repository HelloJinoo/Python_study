from django.db import models

class Post(models.Model):
    title = models.CharField('제목',max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

