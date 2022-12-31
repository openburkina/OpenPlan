from django.urls import path

from .views import ActivityViews,ActivityDetailsViews,ActivitySectorViews,\
        ActivityParticipatingOrgViews,TransactionViews,ConditionActivityViews, ActivityCollaborationTypeViews,IndicatorViews,BudgetViews,\
                TransactionRegionViews,RegionActivityViews, ActivityPlannedDistViews, ActivityResultatViews,ActivityOrganisationTransactionViews,\
                        OrganisationViews,OrganisationActivityViews,OrganisationActivityStatusViews,OrganisationActivityRegionViews,\
                                ActivityChildViews,ActivityDecaissementViews, OrganisationActivitySectorViews, OrganisationActivityRegionTransactionViews, \
                                        ActivityDecaissementEcartViews, HomeActivityStatusViews, HomeEvolutionSectorViews, HomeTransactionRegionTransactionViews,\
                                                HomeTransactionSectorTransactionViews,RegionViews, DecaissementRegionViews, RegionActivityStatusViews,\
                                                        RegionActivityConditionTransactionViews, RegionActivitySectorViews, RegionTransactionSectorTransactionViews, \
                                                                TransactionRecuOrganisationViews, TransactionEmiseOrganisationViews

projet_list = ActivityViews.as_view({'get': 'list'})
projet_detail = ActivityDetailsViews.as_view({'get': 'retrieve'})
organisation_list = OrganisationViews.as_view({'get': 'list'})
country_list = RegionViews.as_view({'get': 'list'})

urlpatterns = [
        path(r'', projet_list, name='projet-list'),
        path(r'<int:pk>', projet_detail, name='projet-details'),
        path(r'<int:activity_id>/child/', ActivityChildViews.as_view(), name='activity-child'),
        path(r'<int:activity_id>/sector/', ActivitySectorViews.as_view(), name='activity-sector'),
        path(r'<int:activity_id>/organisme/', ActivityParticipatingOrgViews.as_view(), name='activity-organisme'),
        path(r'<int:activity_id>/transaction/', TransactionViews.as_view(), name='activity-transaction'),
        path(r'<int:activity_id>/condition/', ConditionActivityViews.as_view(), name='activity-condition'),
        path(r'<int:activity_id>/collaboration/', ActivityCollaborationTypeViews.as_view(), name='activity-collaboration'),
        path(r'<int:activity_id>/indicateur/', IndicatorViews.as_view(), name='activity-indicator'),
        path(r'<int:activity_id>/budget/', BudgetViews.as_view(), name='activity-budget'),
        path(r'<int:activity_id>/contribution/', ActivityOrganisationTransactionViews.as_view(), name='activity-contribution'),
        path(r'<int:activity_id>/plannedDist/', ActivityPlannedDistViews.as_view(), name='activity-plandistribution'),
        path(r'<int:activity_id>/decaissement/', ActivityDecaissementViews.as_view(), name='activity-decaissement'),
        path(r'<int:activity_id>/decaissementecart/', ActivityDecaissementEcartViews.as_view(), name='activity-decaissement-ecart'),
        path(r'<int:activity_id>/results/', ActivityResultatViews.as_view(), name='activity-result'),
        path(r'region/', country_list, name='country-list'),
        path(r'<int:region_id>/region/transaction', TransactionRegionViews.as_view(), name='region-transaction'),
        path(r'<int:region_id>/region/decaissement', DecaissementRegionViews.as_view(), name='region-decaissement'),
        path(r'<int:region_id>/region/activite', RegionActivityViews.as_view(), name='region-activity'),
        path(r'<int:region_id>/region/by_status', RegionActivityStatusViews.as_view(), name='region-activite-bystatus-list'),
        path(r'<int:region_id>/region/by_condition', RegionActivityConditionTransactionViews.as_view(), name='region-activite-organisme-sum'),
        path(r'<int:region_id>/region/by_sector', RegionActivitySectorViews.as_view(), name='region-activite-sector-sum'),
        path(r'<int:region_id>/region/by_sectortransact', RegionTransactionSectorTransactionViews.as_view(), name='region-activite-sector-transact-sum'),
        path(r'organisation/', organisation_list, name='organisation-list'),
        path(r'<int:organisation_id>/organisation/activite/', OrganisationActivityViews.as_view(), name='organisation-activite'),

        path(r'<int:organisation_id>/organisation/transactionr/', TransactionRecuOrganisationViews.as_view(), name='organisation-transaction-recu'),
        path(r'<int:organisation_id>/organisation/transactione/', TransactionEmiseOrganisationViews.as_view(), name='organisation-transaction-emise'),

        path(r'<int:organisation_id>/organisation/by_status', OrganisationActivityStatusViews.as_view(), name='oraganisation-activite-bystatus-list'),
        path(r'<int:organisation_id>/organisation/by_region', OrganisationActivityRegionViews.as_view(), name='oraganisation-activite-region-sum'),
        path(r'<int:organisation_id>/organisation/by_sector', OrganisationActivitySectorViews.as_view(), name='oraganisation-activite-sector-sum'),
        path(r'<int:organisation_id>/organisation/by_regiontransact', OrganisationActivityRegionTransactionViews.as_view(), name='oraganisation-activite-region-transact-sum'),
        path(r'homeactivity/by_status', HomeActivityStatusViews.as_view(), name='home-activity'),
        path(r'homeactivity/by_sector', HomeEvolutionSectorViews.as_view(), name='home-sector'),
        path(r'homeactivity/by_regiontransact', HomeTransactionRegionTransactionViews.as_view(), name='home-region-transaction'),
        path(r'homeactivity/by_sectortransact', HomeTransactionSectorTransactionViews.as_view(), name='home-sector-transaction'),

]
