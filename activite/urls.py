from django.conf.urls import url

from activite.views import DeviseList, DeviseDetail, EtiquetteList, EtiquetteDetail, SourceFinancementList, \
    SourceFinancementDetail, StructureResponsableList, StructureResponsableDetail, ProgrammePhysiqueList, \
    ProgrammePhysiqueDetail, ActivitesList, ActivitesDetail
from generiquemodel.views import select_element_parent

urlpatterns = [
    url(r'^generic/$', select_element_parent),
    url('devise-list/', DeviseList.as_view()),
    url('etiquette-list/', EtiquetteList.as_view()),
    url('sourceFinancement-list/', SourceFinancementList.as_view()),
    url('structureResponsable-list/', StructureResponsableList.as_view()),
    url('programmePhysique-list/', ProgrammePhysiqueList.as_view()),
    url('activites-list/', ActivitesList.as_view()),
    url(r'^devise-detail/$', DeviseDetail.as_view()),
    url(r'^etiquette-detail/$', EtiquetteDetail.as_view()),
    url(r'^sourceFinancement-detail/$', SourceFinancementDetail.as_view()),
    url(r'^structureResponsable-detail/$', StructureResponsableDetail.as_view()),
    url(r'^programmePhysique-detail/$', ProgrammePhysiqueDetail.as_view()),
    url(r'^activites-detail/$', ActivitesDetail.as_view()),
]
