from rest_framework import serializers

from generiquemodel.models import Annee, Structure, Niveau, GenericTable


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = ['id', 'nom', 'budjet']


class AnneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annee
        fields = ['id', 'annee']


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ['id', 'niveau']


class GenericTableSerializer(serializers.ModelSerializer):
    structure = serializers.StringRelatedField(many=True)
    annee = serializers.StringRelatedField(many=True)

    class Meta:
        model = GenericTable
        fields = ['id', 'intitule', 'niveau', 'code', 'structure', 'annee', 'element_parent']
