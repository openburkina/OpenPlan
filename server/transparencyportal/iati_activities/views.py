from datetime import datetime

from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Sum,Count
from django.db.models.expressions import F, Value

from iati_activities.models import Activity,ActivitySector,ActivityOrganization,ActivityParticipatingOrg, \
    Transaction,ConditionActivity,ActivityCollaborationType, Indicator, Budget, Results, PlannedDisbursement

from iati_activities.serializers import ActivitySerializer, ActivityDetailsSerializer,ActivitySectorSerializer,ActivityOrganizationSerializer,\
    ActivityParticipatingOrgSerializer,TransactionSerializer,ConditionActivitySerializer,ActivityCollaborationTypeSerializer, IndicatorSerializer, BudgetSerializer, \
        ResultsSerializer, PlannedDisbursementSerializer,TransactionActivitySerializer, OrganisationActivityByStatusSerializer,\
            OrganisationActivityByRegionSerializer

from iati_referentiel.serializers import OrganizationSerializer

from iati_referentiel.models import Organization


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ActivityViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class OrganisationViews(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ActivityDetailsViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivityDetailsSerializer

class ActivitySectorViews(APIView):
    def get(self, request, activity_id):
        queryset = ActivitySector.objects.filter(activityid=activity_id)
        data = ActivitySectorSerializer(queryset, many=True, context={'request': request}).data
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


class ActivityOrganisationTransactionViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id, transaction_type='Incoming Funds')
        queryset = queryset.annotate(name=F('organizationid2__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'),
                                   currency=F('currency'),
                                   )
        data = TransactionActivitySerializer(queryset, many=True).data
        return Response(data)

class OrganisationActivityViews(APIView):
    def get(self, request, organisation_id):
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id)
        data = ActivityOrganizationSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class OrganisationActivityStatusViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        sting_date_deb = year+'-01-01'
        string_date_fin = year+'-12-31'
        debut = datetime.strptime(sting_date_deb,'%Y-%m-%d').date()
        fin = datetime.strptime(string_date_fin,'%Y-%m-%d').date()
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id, activityid__activitydate__planned_start__range=(debut,fin))
        output = {
            'Identification': 0,
            'Implementation': 0,
            'Finalisation': 0,
            'Closed': 0,
            'Cancelled': 0,
            'Suspended': 0,
            'total': queryset.count(),
        }
        for query in queryset:
            output[query.activityid.activity_status] += 1
        data = OrganisationActivityByStatusSerializer(output).data
        return Response(data)

class OrganisationActivityRegionViews(APIView):
    def get(self, request, organisation_id):
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id,)
        queryset = queryset.annotate(
            regionid3=F('activityid__regionid3__id'),
            name=F('activityid__regionid3_continent')
        ).values('name', 'regionid3')
        #queryset = queryset.annotate(regionid3=F('activityid__regionid3')).values('activityid__regionid3')
        queryset = queryset.annotate(total=Count('activityid__activity__regionid3')).values('total')
        data = OrganisationActivityByRegionSerializer(queryset, many=True).data
        return Response(data)

