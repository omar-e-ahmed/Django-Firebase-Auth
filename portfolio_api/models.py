from django.db import models

# Create your models here.

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # stocks = models.ManyToManyRelation(Stock)
    # url = models.URLField(blank=True)
    def __str__(self):
        return self.name