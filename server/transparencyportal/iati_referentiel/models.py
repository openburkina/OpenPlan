from django.db import models

class Region(models.Model):
    continent = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'

class Organization(models.Model):
    ref = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organization'

class Location(models.Model):
    countryid3 = models.ForeignKey(Country, models.DO_NOTHING, db_column='countryid3')
    ref = models.CharField(max_length=255, blank=True, null=True)
    location_reach = models.CharField(db_column='Location-reach', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    activity_location = models.CharField(db_column='Activity-location', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    administrative_code = models.IntegerField(db_column='Administrative-code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    administrative_level = models.CharField(db_column='Administrative-level', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pos = models.CharField(max_length=255, blank=True, null=True)
    location_class = models.CharField(db_column='Location-class', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'location'


class DefaultAidType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default-aid-type'

class Country(models.Model):
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid')
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'

class CollaborationType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collaboration-type'

class DefaultFinanceType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Default-finance-type'

class HumanitarianScope(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Humanitarian-scope'

class Sector(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.FloatField()
    narrative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'

# Create your models here.
