from django.shortcuts import render

# Create your views here.
from django.db import connection
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from generiquemodel.models import GenericTable, Structure, Annee, Niveau
from generiquemodel.serializers import GenericTableSerializer, StructureSerializer, AnneeSerializer, NiveauSerializer


class StructureList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        structure = Structure.objects.all()
        serializer = StructureSerializer(structure, many=True)
        return JsonResponse(serializer.data, safe=False)


class StructureDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Structure.objects.get(id=id)

        except Structure.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        structure = self.get_object(id=id)
        serializer = StructureSerializer(structure)
        return JsonResponse(serializer.data, safe=False)


class AnneeList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        structure = Annee.objects.all()
        serializer = AnneeSerializer(structure, many=True)
        return JsonResponse(serializer.data, safe=False)


class NiveauList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        niveau = Niveau.objects.all()
        serializer = NiveauSerializer(niveau, many=True)
        return JsonResponse(serializer.data, safe=False)


class NiveauDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Niveau.objects.get(id=id)

        except Niveau.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        niveau = self.get_object(id=id)
        serializer = NiveauSerializer(niveau)
        return JsonResponse(serializer.data, safe=False)


class AnneeDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return Annee.objects.get(id=id)

        except Annee.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        annee = self.get_object(id=id)
        serializer = AnneeSerializer(annee)
        return JsonResponse(serializer.data, safe=False)


class GenericTableList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request):
        generictable = GenericTable.objects.all()
        serializer = GenericTableSerializer(generictable, many=True)
        return JsonResponse(serializer.data, safe=False)


class GenericTableDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get_object(id):
        try:
            return GenericTable.objects.get(id=id)

        except GenericTable.DoesNotExist:
            raise Http404

    def get(self, request):
        id = request.GET.get('id')
        generictable = self.get_object(id=id)
        serializer = GenericTableSerializer(generictable)
        return JsonResponse(serializer.data, safe=False)


def select_element_parent(request):
    if request.method == 'GET' and request.is_ajax():
        id_niveau = request.GET.get('id_niveau')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM generiquemodel_generictable WHERE niveau_id = %s", [id_niveau])
            row = cursor.fetchall()
            return JsonResponse(row, safe=False)
