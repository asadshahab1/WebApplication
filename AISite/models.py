from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Visitor(User):
    gender = models.CharField(max_length=7)
