from django.db import models


class Members(models.Model):
  numero = models.IntegerField()
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
