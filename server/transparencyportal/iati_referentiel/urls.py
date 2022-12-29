from django.urls import path

from .views import OrganizationViews


urlpatterns = [
        path(r'', OrganizationViews.as_view(), name='bailleur-list'),

        ]