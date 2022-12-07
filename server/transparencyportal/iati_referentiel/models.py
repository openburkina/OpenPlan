from django.db import models

class Region(models.Model):
    continent = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name ='Nom')
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'
        verbose_name = 'Région'
        verbose_name_plural = 'Régions'
    def __str__(self):
        return '%s - %s' % (self.continent, self.name)

class Organization(models.Model):
    ref = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organization'
        verbose_name = 'Organisation'
        verbose_name_plural = 'Organisations'

class Location(models.Model):
    countryid3 = models.ForeignKey('Country', models.DO_NOTHING, db_column='countryid3',verbose_name ='Pays')
    ref = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Réference')
    location_reach = models.CharField(db_column='Location-reach', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name ='Nom')
    description = models.CharField(max_length=255, blank=True, null=True)
    activity_location = models.CharField(db_column='Activity-location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    administrative_code = models.IntegerField(db_column='Administrative-code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    administrative_level = models.CharField(db_column='Administrative-level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos = models.CharField(max_length=255, blank=True, null=True)
    location_class = models.CharField(db_column='Location-class', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'location'
        verbose_name = 'Localité'
        verbose_name_plural = 'Localités'
    def __str__(self):
        return '%s - %s' % (self.code, self.name)
    @property
    def country(self):
        return self.countryid3.name


class DefaultAidType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default-aid-type'
        verbose_name = "Type d'aide"
        verbose_name_plural = "Type d'aides"

class Country(models.Model):
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid',verbose_name ='Région')
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True,verbose_name ='Nom')
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'
    def __str__(self):
        return '%s - %s' % (self.code, self.name)

class CollaborationType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collaboration-type'
        verbose_name = 'Type Collaboration'
        verbose_name_plural = 'Type Collaborations'

class DefaultFinanceType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Default-finance-type'
        verbose_name = 'Type Financement'
        verbose_name_plural = 'Type Financements'

class HumanitarianScope(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Humanitarian-scope'
        verbose_name = 'Portée humanitaire'
        verbose_name_plural = 'Portée humanitaires'
        
class Sector(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.FloatField(verbose_name ='Pourcentage')
    narrative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'
        verbose_name = 'Secteur'
        verbose_name_plural = 'Secteurs'

class Tag(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tag'
        verbose_name = 'Etiquette'
        verbose_name_plural = 'Etiquettes'

class Condition(models.Model):
    attached = models.BooleanField()
    condition = models.CharField(db_column='Condition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Condition'
        verbose_name = 'Condition'
        verbose_name_plural = 'Conditions'

# Create your models here.
