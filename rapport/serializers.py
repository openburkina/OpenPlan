from rest_framework import serializers

from rapport.models import Taux


class TauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taux
        fields = ['id', 'activite', 'trimestre', 'taux']
