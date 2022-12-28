from datetime import datetime

from django.shortcuts import get_object_or_404
from iati_activities.models import Activity,ActivitySector,ActivityOrganization,ActivityParticipatingOrg, Transaction
from iati_activities.serializers import ActivitySerializer, ActivityDetailsSerializer,ActivitySectorSerializer,ActivityOrganizationSerializer,ActivityParticipatingOrgSerializer,TransactionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ActivityViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetailsViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivityDetailsSerializer

class ActivitySectorViews(APIView):
    def get(self, request, activity_id):
        queryset = ActivitySector.objects.filter(activityid=activity_id)
        data = ActivitySectorSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityOrganisationViews(APIView):
    def get(self, request, activity_id):
        queryset = ActivityOrganization.objects.filter(activityid=activity_id)
        data = ActivityOrganizationSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityParticipatingOrgViews(APIView):
    def get(self, request, activity_id):
        queryset = ActivityParticipatingOrg.objects.filter(activityid=activity_id)
        data = ActivityParticipatingOrgSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class TransactionViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)