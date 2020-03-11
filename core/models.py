from django.db import models

class CheckTime(models.Model):

    """ CheckTime Model Definition """

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
