from django.urls import path

from .views import ActivityViews,ActivityDetailsViews,ActivitySectorViews,\
        ActivityParticipatingOrgViews,TransactionViews,ConditionActivityViews, ActivityCollaborationTypeViews,IndicatorViews,BudgetViews,\
                TransactionRegionViews,ActivityRegionViews, ActivityPlannedDistViews, ActivityResultatViews,ActivityOrganisationTransactionViews,\
                        OrganisationViews,OrganisationActivityViews,OrganisationActivityStatusViews,OrganisationActivityRegionViews

from .views import ActivityViews,ActivityDetailsViews,ActivitySectorViews,ActivityOrganisationViews,ActivityParticipatingOrgViews,TransactionViews,TransactionRegionViews,ActivityRegionViews, ActivityPlannedDistViews, ActivityResultatViews
projet_list = ActivityViews.as_view({'get': 'list'})
projet_detail = ActivityDetailsViews.as_view({'get': 'retrieve'})
organisation_list = OrganisationViews.as_view({'get': 'list'})

urlpatterns = [
        path(r'', projet_list, name='projet-list'),
        path(r'<int:pk>', projet_detail, name='projet-details'),
        path(r'<int:activity_id>/sector/', ActivitySectorViews.as_view(), name='activity-sector'),
        path(r'<int:activity_id>/organisme/', ActivityParticipatingOrgViews.as_view(), name='activity-organisme'),
        path(r'<int:activity_id>/transaction/', TransactionViews.as_view(), name='activity-transaction'),
        path(r'<int:activity_id>/condition/', ConditionActivityViews.as_view(), name='activity-condition'),
        path(r'<int:activity_id>/collaboration/', ActivityCollaborationTypeViews.as_view(), name='activity-collaboration'),
        path(r'<int:activity_id>/indicateur/', IndicatorViews.as_view(), name='activity-indicator'),
        path(r'<int:activity_id>/budget/', BudgetViews.as_view(), name='activity-budget'),
        path(r'<int:activity_id>/contribution/', ActivityOrganisationTransactionViews.as_view(), name='activity-contribution'),
        path(r'<int:activity_id>/plannedDist/', ActivityPlannedDistViews.as_view(), name='activity-plandistribution'),
        path(r'<int:region_id>/region/', TransactionRegionViews.as_view(), name='region-transaction'),
        path(r'<int:region_id>/activityRegion/', ActivityRegionViews.as_view(), name='activity-region'),
        path(r'<int:region_id>/results/', ActivityResultatViews.as_view(), name='activity-result'),
        path(r'organisation/', organisation_list, name='organisation-list'),
        path(r'<int:organisation_id>/activite/', OrganisationActivityViews.as_view(), name='organisation-activite'),
        path(r'<int:organisation_id>/activite/by_status', OrganisationActivityStatusViews.as_view(), name='oraganisation-activite-bystatus-list'),
        path(r'<int:organisation_id>/activite/by_region', OrganisationActivityRegionViews.as_view(), name='oraganisation-activite-region-sum'),

]