from django.contrib import admin
#
# # Register your models here.
from django.utils.html import format_html
from django import forms

from generiquemodel.models import Annee, Niveau, Structure, GenericTable


#
#
class CustomGenericTableModelForm(forms.ModelForm):
    class Meta:
        model = GenericTable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomGenericTableModelForm, self).__init__(*args, **kwargs)
        self.fields['intitule'].label = format_html("Intitulé <span style='color: #FF0000;'>*</span>")
        self.fields['niveau'].label = format_html("Niveau <span style='color: #FF0000;'>*</span>")
        self.fields['code'].label = format_html("Code <span style='color: #FF0000;'>*</span>")
        self.fields['structure'].label = format_html("Structure <span style='color: #FF0000;'>*</span>")
        self.fields['annee'].label = format_html("Année <span style='color: #FF0000;'>*</span>")


class CustomNiveauModelForm(forms.ModelForm):
    class Meta:
        model = Niveau
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomNiveauModelForm, self).__init__(*args, **kwargs)
        self.fields['niveau'].label = format_html("Niveau <span style='color: #FF0000;'>*</span>")


class CustomAnneeModelForm(forms.ModelForm):
    class Meta:
        model = Annee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomAnneeModelForm, self).__init__(*args, **kwargs)
        self.fields['annee'].label = format_html("Année <span style='color: #FF0000;'>*</span>")


class CustomStructureModelForm(forms.ModelForm):
    class Meta:
        model = Structure
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomStructureModelForm, self).__init__(*args, **kwargs)
        self.fields['nom'].label = format_html("Structure <span style='color: #FF0000;'>*</span>")


class AnneeAdmin(admin.ModelAdmin):
    list_display = ('id', 'annee', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'annee', 'date_ajout', 'date_modification')
    list_filter = ('id', 'annee',)
    search_fields = ('annee',)
    form = CustomAnneeModelForm


#
#
admin.site.register(Annee, AnneeAdmin)


#
#
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('id', 'niveau', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'niveau', 'date_ajout', 'date_modification')
    list_filter = ('id', 'niveau',)
    search_fields = ('niveau',)
    form = CustomNiveauModelForm

#


admin.site.register(Niveau, NiveauAdmin)


#
#
class StructureAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'date_ajout', 'date_modification')
    list_display_links = ('id', 'nom', 'date_ajout', 'date_modification')
    list_filter = ('id', 'nom',)
    search_fields = ('nom',)
    form = CustomStructureModelForm


#
#
admin.site.register(Structure, StructureAdmin)


#
#
class GenericTableAdmin(admin.ModelAdmin):
    list_display = ('code', 'intitule', 'element_parent', 'niveau', 'get_structure', 'get_annee')
    list_display_links = ('code', 'intitule', 'element_parent', 'niveau', 'get_structure', 'get_annee')
    list_filter = ('code', 'intitule', 'element_parent', 'niveau', 'structure', 'annee')
    search_fields = ('intitule',)

    class Media:
        js = ('//code.jquery.com/jquery-1.12.4.min.js', 'admin/js/admin/placeholder.js',)

    form = CustomGenericTableModelForm


admin.site.register(GenericTable, GenericTableAdmin)
