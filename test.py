PostgreSQL is available
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoCronCronjoblog(models.Model):
    code = models.CharField(max_length=64)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_success = models.BooleanField()
    message = models.TextField()
    ran_at_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_cron_cronjoblog'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class OcdsAwardsAward(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    contract_period = models.OneToOneField('OcdsMasterTablesPeriod', models.DO_NOTHING, blank=True, null=True)
    value = models.OneToOneField('OcdsMasterTablesValue', models.DO_NOTHING, blank=True, null=True)
    release = models.ForeignKey('OcdsReleaseRelease', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_awards_award'


class OcdsAwardsAwardSuppliers(models.Model):
    award = models.ForeignKey(OcdsAwardsAward, models.DO_NOTHING)
    entity = models.ForeignKey('OcdsMasterTablesEntity', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_awards_award_suppliers'
        unique_together = (('award', 'entity'),)


class OcdsAwardsAwardamendment(models.Model):
    amendment_ptr = models.OneToOneField('OcdsMasterTablesAmendment', models.DO_NOTHING, primary_key=True)
    ref_award = models.ForeignKey(OcdsAwardsAward, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_awards_awardamendment'


class OcdsAwardsAwarddocument(models.Model):
    document_ptr = models.OneToOneField('OcdsMasterTablesDocument', models.DO_NOTHING, primary_key=True)
    ref_award = models.ForeignKey(OcdsAwardsAward, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_awards_awarddocument'


class OcdsAwardsAwarditem(models.Model):
    item_ptr = models.OneToOneField('OcdsMasterTablesItem', models.DO_NOTHING, primary_key=True)
    ref_award = models.ForeignKey(OcdsAwardsAward, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_awards_awarditem'


class OcdsContractsContract(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    date_signed = models.DateTimeField(blank=True, null=True)
    period = models.OneToOneField('OcdsMasterTablesPeriod', models.DO_NOTHING, blank=True, null=True)
    ref_award = models.OneToOneField(OcdsAwardsAward, models.DO_NOTHING)
    value = models.OneToOneField('OcdsMasterTablesValue', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_contracts_contract'


class OcdsContractsContractamendment(models.Model):
    amendment_ptr = models.OneToOneField('OcdsMasterTablesAmendment', models.DO_NOTHING, primary_key=True)
    ref_contract = models.ForeignKey(OcdsContractsContract, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_contracts_contractamendment'


class OcdsContractsContractdocument(models.Model):
    document_ptr = models.OneToOneField('OcdsMasterTablesDocument', models.DO_NOTHING, primary_key=True)
    ref_contract = models.ForeignKey(OcdsContractsContract, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_contracts_contractdocument'


class OcdsContractsContractitem(models.Model):
    item_ptr = models.OneToOneField('OcdsMasterTablesItem', models.DO_NOTHING, primary_key=True)
    ref_contract = models.ForeignKey(OcdsContractsContract, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_contracts_contractitem'


class OcdsContractsContractmilestone(models.Model):
    milestone_ptr = models.OneToOneField('OcdsMasterTablesMilestone', models.DO_NOTHING, primary_key=True)
    ref_contract = models.ForeignKey(OcdsContractsContract, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_contracts_contractmilestone'


class OcdsImplementationImplementation(models.Model):
    contract = models.OneToOneField(OcdsContractsContract, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_implementation_implementation'


class OcdsImplementationImplementationdocument(models.Model):
    document_ptr = models.OneToOneField('OcdsMasterTablesDocument', models.DO_NOTHING, primary_key=True)
    ref_implementation = models.ForeignKey(OcdsImplementationImplementation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_implementation_implementationdocument'


class OcdsImplementationImplementationmilestone(models.Model):
    milestone_ptr = models.OneToOneField('OcdsMasterTablesMilestone', models.DO_NOTHING, primary_key=True)
    ref_implementation = models.ForeignKey(OcdsImplementationImplementation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_implementation_implementationmilestone'


class OcdsImplementationTransaction(models.Model):
    source = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    implementation = models.ForeignKey(OcdsImplementationImplementation, models.DO_NOTHING, blank=True, null=True)
    payee = models.ForeignKey('OcdsMasterTablesEntity', models.DO_NOTHING, blank=True, null=True)
    payer = models.ForeignKey('OcdsMasterTablesEntity', models.DO_NOTHING, blank=True, null=True)
    value = models.OneToOneField('OcdsMasterTablesValue', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_implementation_transaction'


class OcdsMasterTablesAddress(models.Model):
    country_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    locality_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    locality_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_address'


class OcdsMasterTablesAmendment(models.Model):
    date = models.DateTimeField()
    rationale = models.TextField()

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_amendment'


class OcdsMasterTablesBudget(models.Model):
    source = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)
    amount = models.ForeignKey('OcdsMasterTablesValue', models.DO_NOTHING, blank=True, null=True)
    projet = models.ForeignKey('OcdsMasterTablesProjet', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_budget'


class OcdsMasterTablesChange(models.Model):
    property = models.CharField(max_length=255)
    former_value = models.TextField(blank=True, null=True)
    amendment = models.ForeignKey(OcdsMasterTablesAmendment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_change'


class OcdsMasterTablesClassification(models.Model):
    scheme = models.CharField(max_length=255)
    description = models.TextField()
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_classification'


class OcdsMasterTablesContactpoint(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    telephone = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_contactpoint'


class OcdsMasterTablesDocument(models.Model):
    document_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(blank=True, null=True)
    document_format = models.CharField(max_length=255)
    language = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_document'


class OcdsMasterTablesEntity(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(OcdsMasterTablesAddress, models.DO_NOTHING)
    contact_point = models.ForeignKey(OcdsMasterTablesContactpoint, models.DO_NOTHING)
    identifier = models.ForeignKey('OcdsMasterTablesIdentifier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_entity'


class OcdsMasterTablesEntityadditionalidentifier(models.Model):
    identifier_ptr = models.OneToOneField('OcdsMasterTablesIdentifier', models.DO_NOTHING, primary_key=True)
    ref_entity = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_entityadditionalidentifier'


class OcdsMasterTablesIdentifier(models.Model):
    scheme = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_identifier'


class OcdsMasterTablesItem(models.Model):
    description = models.TextField()
    quantity = models.IntegerField()
    classification = models.ForeignKey(OcdsMasterTablesClassification, models.DO_NOTHING, blank=True, null=True)
    unit = models.OneToOneField('OcdsMasterTablesUnit', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_item'


class OcdsMasterTablesItemadditionalclassification(models.Model):
    classification_ptr = models.OneToOneField(OcdsMasterTablesClassification, models.DO_NOTHING, primary_key=True)
    ref_item = models.ForeignKey(OcdsMasterTablesItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_itemadditionalclassification'


class OcdsMasterTablesMilestone(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateField()
    date_modified = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_milestone'


class OcdsMasterTablesMilestonedocument(models.Model):
    document_ptr = models.OneToOneField(OcdsMasterTablesDocument, models.DO_NOTHING, primary_key=True)
    ref_milestone = models.ForeignKey(OcdsMasterTablesMilestone, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_milestonedocument'


class OcdsMasterTablesPeriod(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_period'


class OcdsMasterTablesProjet(models.Model):
    titre_projet = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_projet'


class OcdsMasterTablesUnit(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.OneToOneField('OcdsMasterTablesValue', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_unit'


class OcdsMasterTablesValue(models.Model):
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'ocds_master_tables_value'


class OcdsPlanningPlanning(models.Model):
    raison = models.TextField(blank=True, null=True)
    budget = models.OneToOneField(OcdsMasterTablesBudget, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_planning_planning'


class OcdsPlanningPlanningdocument(models.Model):
    document_ptr = models.OneToOneField(OcdsMasterTablesDocument, models.DO_NOTHING, primary_key=True)
    planning = models.ForeignKey(OcdsPlanningPlanning, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_planning_planningdocument'


class OcdsPlanningPlanningmilestone(models.Model):
    milestone_ptr = models.OneToOneField(OcdsMasterTablesMilestone, models.DO_NOTHING, primary_key=True)
    planning = models.ForeignKey(OcdsPlanningPlanning, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_planning_planningmilestone'


class OcdsReleasePublishedrelease(models.Model):
    release = models.JSONField()
    ref_record = models.ForeignKey('OcdsReleaseRecord', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_release_publishedrelease'


class OcdsReleaseRecord(models.Model):
    ocid = models.CharField(unique=True, max_length=255)
    implementation_address = models.ForeignKey(OcdsMasterTablesAddress, models.DO_NOTHING, blank=True, null=True)
    implementation_value = models.ForeignKey(OcdsMasterTablesValue, models.DO_NOTHING, blank=True, null=True)
    target = models.ForeignKey('OcdsReleaseTarget', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_release_record'


class OcdsReleaseRelease(models.Model):
    ocid = models.CharField(unique=True, max_length=255)
    date = models.DateTimeField()
    tag = models.TextField()  # This field type is a guess.
    initiation_type = models.CharField(max_length=255)
    buyer = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING, blank=True, null=True)
    planning = models.OneToOneField(OcdsPlanningPlanning, models.DO_NOTHING, blank=True, null=True)
    ref_record = models.OneToOneField(OcdsReleaseRecord, models.DO_NOTHING, blank=True, null=True)
    tender = models.OneToOneField('OcdsTenderTender', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_release_release'


class OcdsReleaseRole(models.Model):
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    entity = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING)
    release = models.ForeignKey(OcdsReleaseRelease, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_release_role'


class OcdsReleaseTarget(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ocds_release_target'


class OcdsTenderTender(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    procurement_method = models.CharField(max_length=255, blank=True, null=True)
    procurement_method_rationale = models.TextField(blank=True, null=True)
    award_criteria = models.CharField(max_length=255, blank=True, null=True)
    award_criteria_details = models.TextField(blank=True, null=True)
    submission_method = models.CharField(max_length=255, blank=True, null=True)
    submission_method_details = models.TextField(blank=True, null=True)
    has_enquiries = models.BooleanField()
    eligibility_criteria = models.TextField(blank=True, null=True)
    award_period = models.ForeignKey(OcdsMasterTablesPeriod, models.DO_NOTHING, blank=True, null=True)
    buyer = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING)
    enquiry_period = models.ForeignKey(OcdsMasterTablesPeriod, models.DO_NOTHING, blank=True, null=True)
    min_value = models.ForeignKey(OcdsMasterTablesValue, models.DO_NOTHING, blank=True, null=True)
    procuring_entity = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING, blank=True, null=True)
    tender_period = models.ForeignKey(OcdsMasterTablesPeriod, models.DO_NOTHING, blank=True, null=True)
    value = models.ForeignKey(OcdsMasterTablesValue, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tender'


class OcdsTenderTenderTenderers(models.Model):
    tender = models.ForeignKey(OcdsTenderTender, models.DO_NOTHING)
    entity = models.ForeignKey(OcdsMasterTablesEntity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tender_tenderers'
        unique_together = (('tender', 'entity'),)


class OcdsTenderTenderamendment(models.Model):
    amendment_ptr = models.OneToOneField(OcdsMasterTablesAmendment, models.DO_NOTHING, primary_key=True)
    tender = models.ForeignKey(OcdsTenderTender, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tenderamendment'


class OcdsTenderTenderdocument(models.Model):
    document_ptr = models.OneToOneField(OcdsMasterTablesDocument, models.DO_NOTHING, primary_key=True)
    tender = models.ForeignKey(OcdsTenderTender, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tenderdocument'


class OcdsTenderTenderitem(models.Model):
    item_ptr = models.OneToOneField(OcdsMasterTablesItem, models.DO_NOTHING, primary_key=True)
    tender = models.ForeignKey(OcdsTenderTender, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tenderitem'


class OcdsTenderTendermilestone(models.Model):
    milestone_ptr = models.OneToOneField(OcdsMasterTablesMilestone, models.DO_NOTHING, primary_key=True)
    tender = models.ForeignKey(OcdsTenderTender, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ocds_tender_tendermilestone'


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)
