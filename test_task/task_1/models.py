from django.contrib.postgres.fields import JSONField
from django.db import models


class Data_test(models.Model):
    names = models.JSONField()



