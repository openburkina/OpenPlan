from django.urls import path

from .views import ActivityViews,ActivityDetailsViews,ActivitySectorViews,ActivityOrganisationViews,\
        ActivityParticipatingOrgViews,TransactionViews,ConditionActivityViews, ActivityCollaborationTypeViews,IndicatorViews,BudgetViews,\
                TransactionRegionViews,ActivityRegionViews, ActivityPlannedDistViews, ActivityResultatViews

projet_list = ActivityViews.as_view({'get': 'list'})
projet_detail = ActivityDetailsViews.as_view({'get': 'retrieve'})

urlpatterns = [
        path(r'', projet_list, name='projet-list'),
        path(r'<int:pk>', projet_detail, name='projet-details'),
        path(r'<int:activity_id>/sector/', ActivitySectorViews.as_view(), name='activity-sector'),
        path(r'<int:activity_id>/organisation/', ActivityOrganisationViews.as_view(), name='activity-organization'),
        path(r'<int:activity_id>/organisme/', ActivityParticipatingOrgViews.as_view(), name='activity-organisme'),
        path(r'<int:activity_id>/transaction/', TransactionViews.as_view(), name='activity-transaction'),
        path(r'<int:activity_id>/condition/', ConditionActivityViews.as_view(), name='activity-condition'),
        path(r'<int:activity_id>/collaboration/', ActivityCollaborationTypeViews.as_view(), name='activity-collaboration'),
        path(r'<int:activity_id>/indicateur/', IndicatorViews.as_view(), name='activity-indicator'),
        path(r'<int:activity_id>/budget/', BudgetViews.as_view(), name='activity-budget'),
        path(r'<int:region_id>/region/', TransactionRegionViews.as_view(), name='activity-organisme'),
        path(r'<int:region_id>/activityRegion/', ActivityRegionViews.as_view(), name='activity-transaction'),
        path(r'<int:region_id>/plannedDist/', ActivityPlannedDistViews.as_view(), name='activity-organisme'),
        path(r'<int:region_id>/results/', ActivityResultatViews.as_view(), name='activity-transaction'),

]