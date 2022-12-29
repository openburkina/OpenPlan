from django.urls import path

from .views import ActivityViews,ActivityDetailsViews,ActivitySectorViews,ActivityOrganisationViews,ActivityParticipatingOrgViews,TransactionViews,TransactionRegionViews,ActivityRegionViews, ActivityPlannedDistViews, ActivityResultatViews,TransactionBailleurViews
projet_list = ActivityViews.as_view({'get': 'list'})
projet_detail = ActivityDetailsViews.as_view({'get': 'retrieve'})

urlpatterns = [
        path(r'', projet_list, name='projet-list'),
        path(r'<int:pk>', projet_detail, name='projet-details'),
        path(r'<int:activity_id>/sector/', ActivitySectorViews.as_view(), name='activity-sector'),
        path(r'<int:activity_id>/organisation/', ActivityOrganisationViews.as_view(), name='activity-organization'),
        path(r'<int:activity_id>/organisme/', ActivityParticipatingOrgViews.as_view(), name='activity-organisme'),
        path(r'<int:activity_id>/transaction/', TransactionViews.as_view(), name='activity-transaction'),
        path(r'<int:region_id>/region/', TransactionRegionViews.as_view(), name='transaction-region'),
        path(r'<int:region_id>/activityRegion/', ActivityRegionViews.as_view(), name='activity-region'),
        path(r'<int:region_id>/plannedDist/', ActivityPlannedDistViews.as_view(), name='activity-pannedDis'),
        path(r'<int:organization_id>/contibution/', TransactionBailleurViews.as_view(), name='bailleur-contribution'),


]