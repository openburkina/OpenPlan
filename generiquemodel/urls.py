from django.conf.urls import url

from generiquemodel.views import select_element_parent, GenericTableList, GenericTableDetail, StructureList, \
    StructureDetail, AnneeList, AnneeDetail, NiveauList, NiveauDetail

urlpatterns = [
    url(r'^generic/$', select_element_parent),
    url('annee-list/', AnneeList.as_view()),
    url('niveau-list/', NiveauList.as_view()),
    url('structureList-list/', StructureList.as_view()),
    url('generictable-list/', GenericTableList.as_view()),
    url(r'^annee-detail/$', AnneeDetail.as_view()),
    url(r'^niveau-detail/$', NiveauDetail.as_view()),
    url(r'^structure-detail/$', StructureDetail.as_view()),
    url(r'^generictable-detail/$', GenericTableDetail.as_view()),
]