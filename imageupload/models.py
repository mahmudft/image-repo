import uuid
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()
def user_directory(instance, filename):
    return '{0}/{1}'.format(instance.author.username, filename)


class Images(models.Model):
    fileid = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory())