from django.http import JsonResponse, Http404

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from activite.models import Devise, Etiquette, SourceFinancement, StructureResponsable, ProgrammePhysique, Activites
from activite.serializers import DeviseSerializer, EtiquetteSerializer, SourceFinancementSerializer, \
    StructureResponsableSerializer, ProgrammePhysiqueSerializer, ActivitesSerializer


class DeviseList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        devise = Devise.objects.all()
        serializer = DeviseSerializer(devise, many=True)
        return JsonResponse(serializer.data, safe=False)


class DeviseDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Devise.objects.get(id=id)

        except Devise.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        devise = self.get_object(id=id)
        serializer = DeviseSerializer(devise)
        return JsonResponse(serializer.data, safe=False)


class EtiquetteList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        etiquette = Etiquette.objects.all()
        serializer = EtiquetteSerializer(etiquette, many=True)
        return JsonResponse(serializer.data, safe=False)


class EtiquetteDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Etiquette.objects.get(id=id)

        except Etiquette.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        etiquette = self.get_object(id=id)
        serializer = EtiquetteSerializer(etiquette)
        return JsonResponse(serializer.data, safe=False)


class SourceFinancementList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        sourceFinancement = SourceFinancement.objects.all()
        serializer = SourceFinancementSerializer(sourceFinancement, many=True)
        return JsonResponse(serializer.data, safe=False)


class SourceFinancementDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return SourceFinancement.objects.get(id=id)

        except SourceFinancement.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        sourceFinancement = self.get_object(id=id)
        serializer = SourceFinancementSerializer(sourceFinancement)
        return JsonResponse(serializer.data, safe=False)


class StructureResponsableList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        structureResponsable = StructureResponsable.objects.all()
        serializer = StructureResponsableSerializer(structureResponsable, many=True)
        return JsonResponse(serializer.data, safe=False)


class StructureResponsableDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return StructureResponsable.objects.get(id=id)

        except StructureResponsable.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        structureResponsable = self.get_object(id=id)
        serializer = StructureResponsableSerializer(structureResponsable)
        return JsonResponse(serializer.data, safe=False)


class ProgrammePhysiqueList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        programmePhysique = ProgrammePhysique.objects.all()
        serializer = ProgrammePhysiqueSerializer(programmePhysique, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProgrammePhysiqueDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return ProgrammePhysique.objects.get(id=id)

        except ProgrammePhysique.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        programmePhysique = self.get_object(id=id)
        serializer = ProgrammePhysiqueSerializer(programmePhysique)
        return JsonResponse(serializer.data, safe=False)


class ActivitesList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        activites = Activites.objects.all()
        serializer = ActivitesSerializer(activites, many=True)
        return JsonResponse(serializer.data, safe=False)


class ActivitesDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Activites.objects.get(id=id)

        except Activites.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        activites = self.get_object(id=id)
        serializer = ActivitesSerializer(activites)
        return JsonResponse(serializer.data, safe=False)