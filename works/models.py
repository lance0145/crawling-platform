from django.db import models

class CreativeWork(models.Model):
    title = models.CharField(max_length=255)
    page_link = models.URLField()
    source = models.CharField(max_length=255)  # e.g., "fmoviesz.to" or "gogoflix.shop"
    retrieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
