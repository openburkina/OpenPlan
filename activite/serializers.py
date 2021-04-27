from rest_framework import serializers

from activite.models import Activites, Devise, Etiquette, SourceFinancement, StructureResponsable, ProgrammePhysique


class DeviseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devise
        fields = ['id', 'devise']


class EtiquetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiquette
        fields = ['id', 'intitule']


class SourceFinancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceFinancement
        fields = ['id', 'source']


class StructureResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = StructureResponsable
        fields = ['id', 'nom']


class ProgrammePhysiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammePhysique
        fields = ['id', 'trimestre']


class ActivitesSerializer(serializers.ModelSerializer):
    financement = serializers.StringRelatedField(many=True)
    structure = serializers.StringRelatedField(many=True)
    pogrammation = serializers.StringRelatedField(many=True)
    etiquette = serializers.StringRelatedField(many=True)

    class Meta:
        model = Activites
        fields = ['id', 'code', 'intitule', 'resultat_attendu',
                  'indicateur', 'cible', 'cout', 'devise', 'financement',
                  'structure', 'pogrammation', 'etiquette', 'generic', 'resultat_atteints',
                  'taux_execution', 'cout_effective', 'observation']
