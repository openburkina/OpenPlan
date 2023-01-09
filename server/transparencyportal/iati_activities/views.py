from datetime import datetime

from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Sum,Count
from django.db.models.expressions import F, Value

from iati_activities.models import Activity,ActivitySector,ActivityOrganization,ActivityParticipatingOrg, \
    Transaction,ConditionActivity,ActivityCollaborationType, Indicator, Budget, Results, PlannedDisbursement,TransactionSector,ActivityLocation,ActivityDate

from iati_activities.serializers import ActivitySerializer, ActivityDetailsSerializer,ActivitySectorSerializer,ActivityOrganizationSerializer,\
    ActivityParticipatingOrgSerializer,TransactionSerializer,ConditionActivitySerializer,ActivityCollaborationTypeSerializer, IndicatorSerializer, BudgetSerializer, \
        ResultsSerializer, PlannedDisbursementSerializer,TransactionActivitySerializer, OrganisationActivityByStatusSerializer,\
            OrganisationActivityByRegionSerializer, OrganisationActivityBySectorSerializer, OrganisationActivityByRegionTransactionSerializer, TransactionEcartSerializer, \
                HomeActivityByStatusSerializer, LocationSerializer, RegActivitySerializer, RegionActivityByStatusSerializer

from iati_referentiel.serializers import OrganizationSerializer

from iati_referentiel.models import Organization,\
        Location

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ActivityViews(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.filter(hierarchy=1)
    serializer_class = ActivitySerializer

class OrganisationViews(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class RegionViews(viewsets.ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

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

class RegionActivityViews(APIView):
    def get(self, request, region_id):
        queryset = ActivityLocation.objects.filter(locationid=region_id)
        data = RegActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class TransactionRegionViews(APIView):
    def get(self, request, region_id):
        queryset = Transaction.objects.filter(activityid__activitylocation__locationid=region_id)
        queryset = queryset.annotate(name=F('organizationid2__narrative')).values('name')
        queryset =  queryset.annotate(value=Sum('value'), currency=F('currency'))                
        data = TransactionActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class DecaissementRegionViews(APIView):
    def get(self, request, region_id):
        queryset = Transaction.objects.filter(activityid__activitylocation__locationid=region_id, transaction_type='Disbursment')
        queryset = queryset.annotate(name=F('organizationid2__narrative')).values('name')
        queryset =  queryset.annotate(value=Sum('value'), currency=F('currency'))                
        data = TransactionActivitySerializer(queryset, many=True, context={'request': request}).data
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
#Activite Transaction Emise
class TransactionEmiseOrganisationViews(APIView):
    def get(self, request, organisation_id):
        queryset = Transaction.objects.filter(organizationid2=organisation_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

#Activite Transaction Recu
class TransactionRecuOrganisationViews(APIView):
    def get(self, request, organisation_id):
        queryset = Transaction.objects.filter(organizationid=organisation_id)
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

#Activite d'une organisation
class OrganisationActivityViews(APIView):
    def get(self, request, organisation_id):
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id)
        data = ActivityOrganizationSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

#Decaissement Activité
class ActivityDecaissementEcartViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id, transaction_type='Disbursement')
        queryset = queryset.annotate(valuedisbursement=Sum('value')).annotate(valueprevue=Sum('activityid__planneddisbursement__value')).annotate(difference=Sum('value')-Sum('activityid__planneddisbursement__value'))
        data = TransactionEcartSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)


#By Organisation And Status
class OrganisationActivityStatusViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id, activityid__activitydate__planned_start__year=year)
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

#By Organisation And Region
class OrganisationActivityRegionViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id, activityid__activitydate__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__regionid3__name')).values('name')
        queryset = queryset.annotate(value=Count('activityid__regionid3__name'))
        data = OrganisationActivityByRegionSerializer(queryset, many=True).data
        return Response(data)

class ActivityChildViews(APIView):
    def get(self, request, activity_id):
        queryset = Activity.objects.filter(activityid=activity_id)
        data = ActivitySerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

class ActivityDecaissementViews(APIView):
    def get(self, request, activity_id):
        queryset = Transaction.objects.filter(activityid=activity_id, transaction_type='Disbursement')
        data = TransactionSerializer(queryset, many=True, context={'request': request}).data
        return Response(data)

#By Organisation And Sector
class OrganisationActivitySectorViews(APIView):
    def get(self, request, organisation_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = ActivityOrganization.objects.filter(
            organizationid=organisation_id, 
            activityid__activitydate__planned_start__year__gte=start_year, 
            activityid__activitydate__planned_start__year__lte=end_year
            ).values('activityid__activitydate__planned_start__year' , name=F('activityid__activitysector__sectorid__narrative')).\
            annotate(value=Count('activityid__activitysector__sectorid__narrative'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Organisation And Region AND Transaction
class OrganisationActivityRegionTransactionViews(APIView):
    def get(self, request, organisation_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityOrganization.objects.filter(organizationid=organisation_id, activityid__activitydate__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__transaction__regionid3__name')).values('name')
        queryset = queryset.annotate(value=Sum('activityid__transaction__value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)


#By Home And Status
class HomeActivityStatusViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityDate.objects.filter(planned_start__year=year)
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
        data = HomeActivityByStatusSerializer(output).data
        return Response(data)


#By Home Evolution And Sector
class HomeEvolutionSectorViews(APIView):
    def get(self, request):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = Activity.objects.filter(
            activityid__activitydate__planned_start__year__gte=start_year, 
            activityid__activitydate__planned_start__year__lte=end_year
            ).values('activityid__activitydate__planned_start__year' , name=F('activityid__activitysector__sectorid__narrative')).\
            annotate(value=Count('activityid__activitysector__sectorid__narrative'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Home And Region AND Transaction
class HomeTransactionRegionTransactionViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Activity.objects.filter(activityid__activitydate__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__activitylocation__locationid__name')).values('name')
        queryset = queryset.annotate(value=Sum('activityid__transaction__value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Home And Sector AND Transaction
class HomeTransactionSectorTransactionViews(APIView):
    def get(self, request):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = TransactionSector.objects.filter(sectorid__activitysector__activityid__activitydate__planned_start__year=year)
        queryset = queryset.annotate(name=F('sectorid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('transactionid__value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Region And Status
class RegionActivityStatusViews(APIView):
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityLocation.objects.filter(locationid=region_id, activityid__activitydate__planned_start__year=year)
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
        data = RegionActivityByStatusSerializer(output).data
        return Response(data)

#By Region And Sector
class RegionActivitySectorViews(APIView):
    def get(self, request, region_id):
        start_year = self.request.query_params.get('start_year')
        end_year = self.request.query_params.get('end_year')
        queryset = ActivityLocation.objects.filter(
            locationid=region_id, 
            activityid__activitydate__planned_start__year__gte=start_year, 
            activityid__activitydate__planned_start__year__lte=end_year
            ).values('activityid__activitydate__planned_start__year' , name=F('activityid__activitysector__sectorid__narrative')).\
            annotate(value=Count('activityid__activitysector__sectorid__narrative'))
        data = OrganisationActivityBySectorSerializer(queryset, many=True).data
        return Response(data)

#By Region AND Transaction
class RegionActivityConditionTransactionViews(APIView):
    def get(self, request, region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = ActivityLocation.objects.filter(locationid=region_id, activityid__activitydate__planned_start__year=year)
        queryset = queryset.annotate(name=F('activityid__organizationid__Organization__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('activityid__transaction__value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)

#By Home And Sector AND Transaction
class RegionTransactionSectorTransactionViews(APIView):
    def get(self, request,region_id):
        year = self.request.query_params.get('year')
        if year is None:
            return Response('Year not specified', status=500)
        queryset = Budget.objects.filter(activityid__activitydate__planned_start__year=year, activityid__activitylocation__locationid=region_id)
        queryset = queryset.annotate(name=F('sectorid__narrative')).values('name')
        queryset = queryset.annotate(value=Sum('value'))
        data = OrganisationActivityByRegionTransactionSerializer(queryset, many=True).data
        return Response(data)


