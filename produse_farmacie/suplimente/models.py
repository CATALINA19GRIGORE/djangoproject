from django.db import models


class Medicamente(models.Model):
    medicament = models.CharField(max_length=100)
    cantitate = models.CharField(max_length=100, default=0)
    comandat = models.BooleanField(default=False)


    def __str__(self):
        return self.medicament
