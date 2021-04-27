from dataclasses import fields

from django.contrib import admin
from django import forms

# Register your models here.
from django.utils.html import format_html

from activite.models import Devise, Etiquette, SourceFinancement, ProgrammePhysique, Activites, StructureResponsable



class CustomActivitesModelForm(forms.ModelForm):
    class Meta:
        model = Activites
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomActivitesModelForm, self).__init__(*args, **kwargs)
        self.fields['code'].label = format_html("Code <span style='color: #FF0000;'>*</span>")
        self.fields['intitule'].label = format_html("Intitulé <span style='color: #FF0000;'>*</span>")
        self.fields['resultat_attendu'].label = format_html("Résultats attendus <span style='color: #FF0000;'>*</span>")
        self.fields['indicateur'].label = format_html("Indicateur <span style='color: #FF0000;'>*</span>")
        self.fields['cible'].label = format_html("Cible <span style='color: #FF0000;'>*</span>")
        self.fields['cout'].label = format_html("Coût <span style='color: #FF0000;'>*</span>")
        self.fields['devise'].label = format_html("Devise <span style='color: #FF0000;'>*</span>")
        self.fields['financement'].label = format_html("Source financement <span style='color: #FF0000;'>*</span>")
        self.fields['structure'].label = format_html("Structures responsables <span style='color: #FF0000;'>*</span>")
        self.fields['pogrammation'].label = format_html("Pogrammation physique <span style='color: #FF0000;'>*</span>")
        self.fields['generic'].label = format_html("Programme <span style='color: #FF0000;'>*</span>")




class CustomProgrammePhysiquModelForm(forms.ModelForm):
    class Meta:
        model = ProgrammePhysique
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomProgrammePhysiquModelForm, self).__init__(*args, **kwargs)
        self.fields['trimestre'].label = format_html("Trimestre <span style='color: #FF0000;'>*</span>")


class CustomSourceFinancementModelForm(forms.ModelForm):
    class Meta:
        model = SourceFinancement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomSourceFinancementModelForm, self).__init__(*args, **kwargs)
        self.fields['source'].label = format_html("Source Financement <span style='color: #FF0000;'>*</span>")


class CustomDeviseModelForm(forms.ModelForm):
    class Meta:
        model = Devise
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomDeviseModelForm, self).__init__(*args, **kwargs)
        self.fields['devise'].label = format_html("Devise <span style='color: #FF0000;'>*</span>")


class CustomEtiquetteModelForm(forms.ModelForm):
    class Meta:
        model = Etiquette
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomEtiquetteModelForm, self).__init__(*args, **kwargs)
        self.fields['intitule'].label = format_html("Etiquette <span style='color: #FF0000;'>*</span>")


class CustomStructureResponsableModelForm(forms.ModelForm):
    class Meta:
        model = StructureResponsable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomStructureResponsableModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].label = format_html("Structure responsable <span style='color: #FF0000;'>*</span>")


class DeviseAdmin(admin.ModelAdmin):
    list_display = ('id', 'devise', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'devise', 'date_ajout', 'date_modification')
    list_filter = ('id', 'devise',)
    search_fields = ('devise',)
    form = CustomDeviseModelForm


#
#
admin.site.register(Devise, DeviseAdmin)


#
#
class EtiquetteAdmin(admin.ModelAdmin):
    list_display = ('id', 'intitule', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'intitule', 'date_ajout', 'date_modification')
    list_filter = ('id', 'intitule',)
    search_fields = ('intitule',)
    form = CustomEtiquetteModelForm


#
#
admin.site.register(Etiquette, EtiquetteAdmin)


#
#
class SourceFinancementAdmin(admin.ModelAdmin):
    list_display = ('id', 'source', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'source', 'date_ajout', 'date_modification')
    list_filter = ('id', 'source',)
    search_fields = ('source',)
    form = CustomSourceFinancementModelForm


admin.site.register(SourceFinancement, SourceFinancementAdmin)


class StructureResponsableAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'nom', 'date_ajout', 'date_modification')
    list_filter = ('id', 'nom',)
    search_fields = ('nom',)
    form = CustomStructureResponsableModelForm


#
#
admin.site.register(StructureResponsable, StructureResponsableAdmin)


class ProgrammePhysiqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'trimestre', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'trimestre', 'date_ajout', 'date_modification')
    list_filter = ('id', 'trimestre',)
    search_fields = ('trimestre',)
    form = CustomProgrammePhysiquModelForm


#
#
admin.site.register(ProgrammePhysique, ProgrammePhysiqueAdmin)


#
#
class ActivitesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code', 'intitule', 'resultat_attendu', 'indicateur', 'cible', 'cout', 'devise', 'get_financement',
        'get_structure', 'get_pogrammation', 'get_etiquette', 'generic')
    list_display_links = (
        'id', 'code', 'intitule', 'resultat_attendu', 'indicateur', 'cible', 'cout', 'devise', 'get_financement',
        'get_structure', 'get_pogrammation', 'get_etiquette', 'generic')
    list_filter = (
        'id', 'code', 'intitule', 'resultat_attendu', 'indicateur', 'cible', 'cout', 'devise', 'financement',
        'structure',
        'pogrammation', 'etiquette', 'generic')
    search_fields = ('intitule',)

    class Media:
        js = ('//code.jquery.com/jquery-1.12.4.min.js', 'admin/js/admin/placeholder.js',)

    form = CustomActivitesModelForm


admin.site.register(Activites, ActivitesAdmin)
