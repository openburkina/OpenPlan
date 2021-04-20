from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from generiquemodel.models import GenericTable


class Devise(models.Model):
    id = models.AutoField(primary_key=True)
    devise = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.devise


class Etiquette(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.intitule


class SourceFinancement(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source


class StructureResponsable(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class ProgrammePhysique(models.Model):
    id = models.AutoField(primary_key=True)
    trimestre = models.CharField(max_length=255, unique=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Programmations Physique'


    def __str__(self):
        return self.trimestre


class Activites(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.PositiveIntegerField(unique=True)
    intitule = models.CharField(max_length=1000)
    resultat_attendu = models.CharField(max_length=1000)
    indicateur = models.CharField(max_length=255)
    cible = models.PositiveIntegerField()
    cout = models.PositiveBigIntegerField()
    devise = models.ForeignKey(Devise, on_delete=models.CASCADE)
    financement = models.ManyToManyField('SourceFinancement')
    structure = models.ManyToManyField('StructureResponsable')
    pogrammation = models.ManyToManyField('ProgrammePhysique')
    etiquette = models.ManyToManyField('Etiquette', blank=True)
    generic = models.ForeignKey(GenericTable, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Activité'
        verbose_name_plural = 'Activités'

    def get_financement(self):
        return ",".join([str(p) for p in self.financement.all()])

    def get_structure(self):
        return ",".join([str(p) for p in self.structure.all()])

    def get_pogrammation(self):
        return ",".join([str(p) for p in self.pogrammation.all()])

    def get_etiquette(self):
        return ",".join([str(p) for p in self.etiquette.all()])

    def __str__(self):
        return str(self.code) + ' ' + self.intitule
