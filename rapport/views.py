from django.http import JsonResponse

from django.db import connection
from activite.models import Activites
from .models import Taux
from django import forms


def select_trimestre(request):
    if request.method == 'GET' and request.is_ajax():
        id_activite = request.GET.get('id_activite')
        with connection.cursor() as cursor:
            cursor.execute("SELECT activite_activites_pogrammation.id as id, "
                           "activite_programmephysique.trimestre AS trimestre "
                           "FROM activite_activites_pogrammation, "
                           "activite_programmephysique WHERE "
                           "activite_activites_pogrammation.activites_id = %s "
                           "AND activite_activites_pogrammation.programmephysique_id "
                           "= activite_programmephysique.id", [id_activite])
            row = cursor.fetchall()
            return JsonResponse(row, safe=False)
