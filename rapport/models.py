from django.db import models

# Create your models here.
from activite.models import Activites, ProgrammePhysique


class Taux(models.Model):
    id = models.AutoField(primary_key=True)
    activite = models.ForeignKey(Activites, on_delete=models.CASCADE)
    trimestre = models.ForeignKey(ProgrammePhysique, on_delete=models.CASCADE, null=True)
    taux = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.activite)
