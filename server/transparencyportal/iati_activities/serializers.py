from iati_activities.models import Activity,ActivityCollaborationType,ActivityLocation,ActivityOrganization,ActivitySector,ContactInfo,ActivityParticipatingOrg, Transaction, PlannedDisbursement, Results
from iati_referentiel.serializers import CountrySerializer,RegionSerializer,SectorSerializer,OrganizationSerializer
from rest_framework import serializers



class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class ActivityCollaborationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCollaborationType
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

class TransactionSerializer(serializers.ModelSerializer):
    regionid3 = RegionSerializer()
    countryid3 = CountrySerializer()
    organizationid2 = OrganizationSerializer()
    organizationid = OrganizationSerializer()
    class Meta:
        model = Transaction
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