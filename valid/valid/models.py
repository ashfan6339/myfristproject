from django.db import models

from valid.de import validate_even


class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])