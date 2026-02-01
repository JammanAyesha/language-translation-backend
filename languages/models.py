from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    offline_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
