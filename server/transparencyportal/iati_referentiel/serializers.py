from rest_framework import serializers
from iati_referentiel.models import CollaborationType,Condition,Country,DefaultAidType,DefaultFinanceType,HumanitarianScope,Location,Organization,Region,Sector,Tag



class CollaborationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationType
        fields = '__all__'

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class DefaultAidTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultAidType
        fields = '__all__'

class DefaultFinanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultFinanceType
        fields = '__all__'

class HumanitarianScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanitarianScope
        fields = '__all__'
    
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'