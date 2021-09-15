from os import setpriority
from django.db import models
from users.models import User

# django-ckeditor
from ckeditor.fields import RichTextField

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    body = RichTextField(null=True)
    image = models.ImageField(null=True, upload_to='posts')
    published = models.BooleanField(default=True)


    def __str__(self):
        """Return posttitle and user."""
        return f'{self.title} | {self.user.first_name}'