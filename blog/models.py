from django.db import models

class Article(models.Model):
    url = models.URLField(blank=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title