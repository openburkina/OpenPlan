from django.db import models


# Create your models here.
class Annee(models.Model):
    id = models.AutoField(primary_key=True)
    annee = models.PositiveSmallIntegerField(unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Année'

    def __str__(self):
        return str(self.annee)


class Structure(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Niveau(models.Model):
    id = models.AutoField(primary_key=True)
    niveau = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.niveau


class GenericTable(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    code = models.PositiveIntegerField(unique=True)
    structure = models.ManyToManyField('Structure')
    annee = models.ManyToManyField('Annee')
    element_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def get_annee(self):
        return ",".join([str(p) for p in self.annee.all()])

    def get_structure(self):
        return ",".join([str(p) for p in self.structure.all()])

    def __str__(self):
        return str(self.code) + ' ' + self.intitule
