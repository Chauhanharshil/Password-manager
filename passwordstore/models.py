from django.db import models

# Create your models here.
class Passwordstore(models.Model):
    app_name = models.CharField(max_length=50)
    password_field = models.CharField(max_length=50)

    def __str__(self):
        return self.app_name
