# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActivityParticipatingOrg(models.Model):
    role = models.CharField(max_length=255, blank=True, null=True)
    organizationid = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organizationid')
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')

    class Meta:
        managed = False
        db_table = 'Activity-Participating-org'


class ActivityDate(models.Model):
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')
    type = models.CharField(max_length=255, blank=True, null=True)
    planned_start = models.CharField(db_column='Planned-start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    planned_end = models.CharField(db_column='Planned-end', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_start = models.CharField(db_column='Actual-start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_end = models.CharField(db_column='Actual-end', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Activity-date'


class ActivityCollaborationType(models.Model):
    activityid = models.OneToOneField('Activity', models.DO_NOTHING, db_column='activityid', primary_key=True)
    collaboration_typeid = models.ForeignKey('CollaborationType', models.DO_NOTHING, db_column='Collaboration-typeID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Activity_Collaboration-type'
        unique_together = (('activityid', 'collaboration_typeid'),)


class ActivityHumanitarianScope(models.Model):
    activityid = models.OneToOneField('Activity', models.DO_NOTHING, db_column='activityid', primary_key=True)
    humanitarian_scopeid = models.ForeignKey('HumanitarianScope', models.DO_NOTHING, db_column='Humanitarian-scopeID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Activity_Humanitarian-scope'
        unique_together = (('activityid', 'humanitarian_scopeid'),)


class ActualDocumentLink(models.Model):
    actualid = models.OneToOneField('Actual', models.DO_NOTHING, db_column='actualid', primary_key=True)
    document_linkid = models.ForeignKey('DocumentLink', models.DO_NOTHING, db_column='Document-linkID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Actual_Document-link'
        unique_together = (('actualid', 'document_linkid'),)


class BaselineDocumentLink(models.Model):
    baselineid = models.OneToOneField('Baseline', models.DO_NOTHING, db_column='baselineid', primary_key=True)
    document_linkid = models.ForeignKey('DocumentLink', models.DO_NOTHING, db_column='Document-linkID')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Baseline_Document-link'
        unique_together = (('baselineid', 'document_linkid'),)


class CollaborationType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Collaboration-type'


class Condition(models.Model):
    attached = models.BooleanField()
    condition = models.CharField(db_column='Condition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Condition'


class ContactInfo(models.Model):
    organizationid = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organizationid')
    person_name = models.CharField(db_column='Person-name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    job_title = models.CharField(db_column='Job-title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Contact-info'


class DefaultFinanceType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Default-finance-type'


class DefaultFinanceTypeActivity(models.Model):
    default_finance_typeid = models.OneToOneField(DefaultFinanceType, models.DO_NOTHING, db_column='Default-finance-typeID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')

    class Meta:
        managed = False
        db_table = 'Default-finance-type_Activity'
        unique_together = (('default_finance_typeid', 'activityid'),)


class DocumentLink(models.Model):
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')
    url = models.CharField(max_length=255, blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Document-link'


class DocumentLinkIndicator(models.Model):
    document_linkid = models.OneToOneField(DocumentLink, models.DO_NOTHING, db_column='Document-linkID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    indicatorid = models.ForeignKey('Indicator', models.DO_NOTHING, db_column='indicatorid')

    class Meta:
        managed = False
        db_table = 'Document-link_Indicator'
        unique_together = (('document_linkid', 'indicatorid'),)


class DocumentLinkResults(models.Model):
    document_linkid = models.OneToOneField(DocumentLink, models.DO_NOTHING, db_column='Document-linkID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    resultsid = models.ForeignKey('Results', models.DO_NOTHING, db_column='resultsid')

    class Meta:
        managed = False
        db_table = 'Document-link_Results'
        unique_together = (('document_linkid', 'resultsid'),)


class HumanitarianScope(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Humanitarian-scope'


class PlannedDisbursement(models.Model):
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')
    type = models.CharField(max_length=255, blank=True, null=True)
    period_start = models.CharField(db_column='Period-start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.CharField(db_column='Period-end', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField()
    currency = models.CharField(max_length=255, blank=True, null=True)
    value_date = models.CharField(db_column='Value-date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Planned-disbursement'


class Tag(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tag'


class Transaction(models.Model):
    regionid3 = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid3')
    countryid3 = models.ForeignKey('Country', models.DO_NOTHING, db_column='countryid3')
    organizationid2 = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organizationid2')
    organizationid = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organizationid')
    activityid = models.ForeignKey('Activity', models.DO_NOTHING, db_column='activityid')
    ref = models.CharField(max_length=255, blank=True, null=True)
    humanitarian = models.BooleanField()
    transaction_type = models.CharField(db_column='Transaction-type', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_date = models.CharField(db_column='Transaction-date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField()
    currency = models.CharField(max_length=255, blank=True, null=True)
    value_date = models.CharField(db_column='Value-date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.CharField(max_length=255, blank=True, null=True)
    disbursement_channel = models.CharField(db_column='Disbursement-channel', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Transaction'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Activity(models.Model):
    regionid3 = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid3')
    countryid3 = models.ForeignKey('Country', models.DO_NOTHING, db_column='countryid3')
    activityid = models.ForeignKey('self', models.DO_NOTHING, db_column='activityid', blank=True, null=True)
    contact_infoid = models.ForeignKey(ContactInfo, models.DO_NOTHING, db_column='Contact-infoID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_updated_datetime = models.CharField(db_column='Last-updated-datetime', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lang = models.CharField(max_length=255, blank=True, null=True)
    default_currency = models.CharField(db_column='Default-currency', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    humanitarian = models.BooleanField()
    hierarchy = models.IntegerField()
    budget_not_provided = models.CharField(db_column='Budget-not-provided', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    iati_identifier = models.BigIntegerField(db_column='Iati-identifier')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    activity_status = models.CharField(db_column='Activity-status', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activity_scope = models.CharField(db_column='Activity-scope', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_relationship = models.CharField(db_column='Type-relationship', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'activity'


class ActivityLocation(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityid', primary_key=True)
    locationid = models.ForeignKey('Location', models.DO_NOTHING, db_column='locationid')

    class Meta:
        managed = False
        db_table = 'activity_location'
        unique_together = (('activityid', 'locationid'),)


class ActivityOrganization(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityid', primary_key=True)
    organizationid = models.ForeignKey('Organization', models.DO_NOTHING, db_column='organizationid')

    class Meta:
        managed = False
        db_table = 'activity_organization'
        unique_together = (('activityid', 'organizationid'),)


class ActivitySector(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityid', primary_key=True)
    sectorid = models.ForeignKey('Sector', models.DO_NOTHING, db_column='sectorid')

    class Meta:
        managed = False
        db_table = 'activity_sector'
        unique_together = (('activityid', 'sectorid'),)


class ActivityTag(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityid', primary_key=True)
    tagid = models.ForeignKey(Tag, models.DO_NOTHING, db_column='tagid')

    class Meta:
        managed = False
        db_table = 'activity_tag'
        unique_together = (('activityid', 'tagid'),)


class Actual(models.Model):
    value = models.CharField(max_length=255, blank=True, null=True)
    periodid = models.ForeignKey('Period', models.DO_NOTHING, db_column='periodid')

    class Meta:
        managed = False
        db_table = 'actual'


class ActualDimension(models.Model):
    actualid = models.OneToOneField(Actual, models.DO_NOTHING, db_column='actualid', primary_key=True)
    dimensionid = models.ForeignKey('Dimension', models.DO_NOTHING, db_column='dimensionid')

    class Meta:
        managed = False
        db_table = 'actual_dimension'
        unique_together = (('actualid', 'dimensionid'),)


class Baseline(models.Model):
    indicatorid = models.ForeignKey('Indicator', models.DO_NOTHING, db_column='indicatorid')
    year = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'baseline'


class Budget(models.Model):
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid')
    type = models.CharField(max_length=255, blank=True, null=True)
    statusst = models.CharField(max_length=255, blank=True, null=True)
    period_start = models.CharField(db_column='Period-start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.CharField(db_column='Period-end', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    value = models.FloatField()
    currency = models.CharField(max_length=255, blank=True, null=True)
    value_date = models.CharField(db_column='Value-date', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'budget'


class Comment(models.Model):
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class ConditionActivity(models.Model):
    conditionid = models.OneToOneField(Condition, models.DO_NOTHING, db_column='conditionid', primary_key=True)
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid')

    class Meta:
        managed = False
        db_table = 'condition_activity'
        unique_together = (('conditionid', 'activityid'),)


class Country(models.Model):
    regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid')
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'


class DefaultAidType(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default-aid-type'


class DefaultAidTypeActivity(models.Model):
    default_aid_typeid = models.OneToOneField(DefaultAidType, models.DO_NOTHING, db_column='default-aid-typeID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid')

    class Meta:
        managed = False
        db_table = 'default-aid-type_Activity'
        unique_together = (('default_aid_typeid', 'activityid'),)


class Dimension(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dimension'


class Indicator(models.Model):
    resultsid = models.ForeignKey('Results', models.DO_NOTHING, db_column='resultsid')
    measure = models.CharField(max_length=255, blank=True, null=True)
    ascending = models.BooleanField()
    aggregation_status = models.BooleanField(db_column='Aggregation-status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicator'


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


class Organization(models.Model):
    ref = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    narrative = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organization'


class Period(models.Model):
    indicatorid = models.ForeignKey(Indicator, models.DO_NOTHING, db_column='indicatorid')
    period_start = models.CharField(db_column='Period-start', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end = models.CharField(db_column='Period-end', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'period'


class Region(models.Model):
    continent = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    discriminator = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'


class Results(models.Model):
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='activityid')
    type = models.CharField(max_length=255, blank=True, null=True)
    aggregation_status = models.BooleanField(db_column='Aggregation-status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class Sector(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    percentage = models.FloatField()
    narrative = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'




class Target(models.Model):
    locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationid')
    value = models.CharField(max_length=255, blank=True, null=True)
    commentid = models.IntegerField()
    periodid = models.ForeignKey(Period, models.DO_NOTHING, db_column='periodid')

    class Meta:
        managed = False
        db_table = 'target'


class TargetComment2(models.Model):
    targetid = models.OneToOneField(Target, models.DO_NOTHING, db_column='targetid', primary_key=True)
    commentid = models.ForeignKey(Comment, models.DO_NOTHING, db_column='commentid')

    class Meta:
        managed = False
        db_table = 'target_comment2'
        unique_together = (('targetid', 'commentid'),)


class TargetDimension(models.Model):
    targetid = models.OneToOneField(Target, models.DO_NOTHING, db_column='targetid', primary_key=True)
    dimensionid = models.ForeignKey(Dimension, models.DO_NOTHING, db_column='dimensionid')

    class Meta:
        managed = False
        db_table = 'target_dimension'
        unique_together = (('targetid', 'dimensionid'),)


class TransactionSector(models.Model):
    transactionid = models.OneToOneField(Transaction, models.DO_NOTHING, db_column='transactionid', primary_key=True)
    sectorid = models.ForeignKey(Sector, models.DO_NOTHING, db_column='sectorid')

    class Meta:
        managed = False
        db_table = 'transaction_sector'
        unique_together = (('transactionid', 'sectorid'),)


