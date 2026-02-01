from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=10)
    target_language = models.CharField(max_length=10)
    original_text = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "user",
            "source_language",
            "target_language",
            "original_text",
            "translated_text",
        )

    def __str__(self):
        return self.original_text[:30] + "..."
