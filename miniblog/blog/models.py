from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    desc=RichTextField()
    timestamp=models.DateTimeField(default=timezone.now)
    class Meta:
        ordering=['-timestamp']
