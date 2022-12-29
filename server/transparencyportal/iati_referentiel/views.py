from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from iati_referentiel.models import Organization
from iati_referentiel.serializers import OrganizationSerializer
# Create your views here.


class OrganizationViews(APIView):
    def get(self, request):
        queryset = Organization.objects.filter(type='Funding')
        data = OrganizationSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class OrganizationContributionViews(APIView):
    def get(self, request):
        queryset = Organization.objects.filter(type='Funding')
        data = OrganizationSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

