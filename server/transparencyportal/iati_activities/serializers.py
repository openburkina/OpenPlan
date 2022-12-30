from iati_activities.models import Activity,ActivityCollaborationType,ConditionActivity,ActivityOrganization,\
    ActivitySector,ContactInfo,ActivityParticipatingOrg, Transaction, ActivityCollaborationType, Indicator, Results, Budget,\
        PlannedDisbursement

from iati_referentiel.serializers import CountrySerializer,RegionSerializer,SectorSerializer,\
    OrganizationSerializer,ConditionSerializer,CollaborationTypeSerializer


from rest_framework import serializers



class ActivitySerializer(serializers.ModelSerializer):
    regionid3 = RegionSerializer()
    countryid3 = CountrySerializer()
    class Meta:
        model = Activity
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ActivityDetailsSerializer(serializers.ModelSerializer):
    regionid3 = RegionSerializer()
    countryid3 = CountrySerializer()
    activityid = ActivitySerializer()
    contact_infoid = ContactSerializer()

    class Meta:
        model = Activity
        fields = '__all__'

class ActivitySectorSerializer(serializers.ModelSerializer):
    activityid = ActivitySerializer()
    sectorid = SectorSerializer()
    class Meta:
        model = ActivitySector
        fields = '__all__'

class ActivityOrganizationSerializer(serializers.ModelSerializer):
    activityid = ActivitySerializer()
    organizationid = OrganizationSerializer()
    class Meta:
        model = ActivityOrganization
        fields = '__all__'

class ActivityParticipatingOrgSerializer(serializers.ModelSerializer):
    organizationid = OrganizationSerializer()
    class Meta:
        model = ActivityParticipatingOrg
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    regionid3 = RegionSerializer()
    countryid3 = CountrySerializer()
    organizationid2 = OrganizationSerializer()
    organizationid = OrganizationSerializer()
    class Meta:
        model = Transaction
        fields = '__all__'

class ConditionActivitySerializer(serializers.ModelSerializer):
    conditionid = ConditionSerializer()
    class Meta:
        model = ConditionActivity
        fields = '__all__'

class ActivityCollaborationTypeSerializer(serializers.ModelSerializer):
    collaboration_typeid = CollaborationTypeSerializer()
    class Meta:
        model = ActivityCollaborationType
        fields = '__all__'

class IndicatorSerializer(serializers.ModelSerializer):
    resultsid = ResultsSerializer()
    class Meta:
        model = Indicator
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class PlannedDisbursementSerializer(serializers.ModelSerializer):
    activityid = ActivitySerializer()
    class Meta:
        model = PlannedDisbursement
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    activityid = ActivitySerializer()
    class Meta:
        model = Results
        fields = '__all__'

class TransactionActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.FloatField()
    currency = serializers.CharField()

class OrganisationActivityByStatusSerializer(serializers.Serializer):
    Identification = serializers.IntegerField()
    Implementation = serializers.IntegerField()
    Finalisation = serializers.IntegerField()
    Closed = serializers.IntegerField()
    Cancelled = serializers.IntegerField()
    Suspended = serializers.IntegerField()
    total = serializers.IntegerField()

class OrganisationActivityByRegionSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()

class OrganisationActivityBySectorSerializer(serializers.Serializer):
    planned_start = serializers.IntegerField(source='activityid__activitydate__planned_start__year')
    name = serializers.CharField()
    value = serializers.IntegerField()

class OrganisationActivityByRegionTransactionSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.IntegerField()

class TransactionEcartSerializer(serializers.Serializer):
    valuedisbursement = serializers.FloatField()
    valueprevue = serializers.FloatField()
    difference = serializers.FloatField()

class HomeActivityByStatusSerializer(serializers.Serializer):
    Identification = serializers.IntegerField()
    Implementation = serializers.IntegerField()
    Finalisation = serializers.IntegerField()
    Closed = serializers.IntegerField()
    Cancelled = serializers.IntegerField()
    Suspended = serializers.IntegerField()
    total = serializers.IntegerField()