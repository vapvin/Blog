from django.db import models
from core import models as core_models

class Post(core_models.CheckTime):

    """ Post Model Definition """

    name = models.CharField(max_length=140)
    content = models.TextField()