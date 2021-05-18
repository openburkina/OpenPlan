# from django.contrib import admin
#
# # Register your models here.
# from django import forms
# from django.utils.html import format_html
#
# from activite.models import Activites
# from rapport.models import Taux
#
#
# class CustomTauxModelForm(forms.ModelForm):
#     class Meta:
#         model = Taux
#         fields = '__all__'
#
#     def __init__(self, *args, **kwargs):
#         super(CustomTauxModelForm, self).__init__(*args, **kwargs)
#         self.fields['activite'].label = format_html("Activie <span style='color: #FF0000;'>*</span>")
#
#
# class TauxAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('//code.jquery.com/jquery-1.12.4.min.js', 'admin/js/admin/placeholder.js',)
#
#     form = CustomTauxModelForm
#
#
# admin.site.register(Taux, TauxAdmin)
