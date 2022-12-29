from datetime import datetime

from django.shortcuts import get_object_or_404

from iati_activities.models import Activity,ActivitySector,ActivityOrganization,ActivityParticipatingOrg, \
    Transaction,ConditionActivity,ActivityCollaborationType, Indicator, Budget, Results, PlannedDisbursement

from iati_activities.serializers import ActivitySerializer, ActivityDetailsSerializer,ActivitySectorSerializer,ActivityOrganizationSerializer,\
    ActivityParticipatingOrgSerializer,TransactionSerializer,ConditionActivitySerializer,ActivityCollaborationTypeSerializer, IndicatorSerializer, BudgetSerializer, \
        ResultsSerializer, PlannedDisbursementSerializer


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

class ConditionActivityViews(APIView):
    def get(self, request, activity_id):
        queryset = ConditionActivity.objects.filter(activityid=activity_id)
        data = ConditionActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityCollaborationTypeViews(APIView):
    def get(self, request, activity_id):
        queryset = ActivityCollaborationType.objects.filter(activityid=activity_id)
        data = ActivityCollaborationTypeSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class IndicatorViews(APIView):
    def get(self, request, activity_id):
        queryset = Indicator.objects.filter(resultsid__activityid=activity_id)
        data = IndicatorSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class BudgetViews(APIView):
    def get(self, request, activity_id):
        queryset = Budget.objects.filter(resultsid__activityid=activity_id)
        data = BudgetSerializer(queryset, many=True, context={'request': request}).data

class ActivityRegionViews(APIView):
    def get(self, request, region_id):
        queryset = Activity.objects.filter(regionid3=region_id)
        data = ActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class TransactionRegionViews(APIView):
    def get(self, request, region_id):
        queryset = Transaction.objects.filter(regionid3=region_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class TransactionBailleurViews(APIView):
    def get(self, request, organization_id):
        queryset = Transaction.objects.filter(organizationid2=organization_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityResultatViews(APIView):
    def get(self, request, activity_id):
        queryset = Results.objects.filter(activityid=activity_id)
        data = ResultsSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityPlannedDistViews(APIView):
    def get(self, request, activity_id):
        queryset = PlannedDisbursement.objects.filter(activityid=activity_id)
        data = PlannedDisbursementSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)