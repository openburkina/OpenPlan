from django.contrib import admin

from iati_referentiel.models import CollaborationType, Country, DefaultAidType, DefaultFinanceType, \
HumanitarianScope, Location, Organization, Region, Sector, Tag, Condition

from iati_activities.admin import Contactline,Period,TargetComment2,TargetDimension,Comment,Dimension,DocumentLink,ContactInfo

class CollaborationTypeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)
    list_per_page=10

class CountryAdmin(admin.ModelAdmin):
    list_display = ('regionid','code','name','discriminator')
    search_fields = ('regionid','code','name')
    list_filter = ('regionid','code','name')
    list_per_page=10

class DefaultAidTypeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)
    list_per_page=10

class DefaultFinanceTypeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)
    list_per_page=10

class HumanitarianScopeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)
    list_filter = ('type',)
    list_per_page=10

class LocationAdmin(admin.ModelAdmin):
    list_display = ('countryid3','ref','location_reach','code','name','description','activity_location','administrative_code','administrative_level','pos','location_class')
    search_fields = ('countryid3','ref','location_reach','code','name')
    list_filter = ('countryid3','ref','location_reach','code','name')
    list_per_page=10

class RegionAdmin(admin.ModelAdmin):
    list_display = ('continent','name','discriminator')
    search_fields = ('continent','name')
    list_filter = ('continent','name')
    list_per_page=10

class SectorAdmin(admin.ModelAdmin):
    list_display = ('code','percentage','narrative')
    search_fields = ('code',)
    list_filter = ('code',)
    list_per_page=10

class TagAdmin(admin.ModelAdmin):
    list_display = ('code','narrative')
    search_fields = ('code',)
    list_filter = ('code',)
    list_per_page=10

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('attached','condition','type')
    search_fields = ('condition', 'type')
    list_filter = ('attached',)
    list_per_page=10

class DefaultAidTypeline(admin.StackedInline):
    model = DefaultAidType
    extra = 0

class CollaborationTypeline(admin.StackedInline):
    model = CollaborationType
    extra = 0

class Conditionline(admin.StackedInline):
    model = Condition
    extra = 0

class Countryline(admin.StackedInline):
    model = Country
    extra = 0

class DefaultFinanceTypeline(admin.StackedInline):
    model = DefaultFinanceType
    extra = 0

class HumanitarianScopeline(admin.StackedInline):
    model = HumanitarianScope
    extra = 0

admin.site.register(CollaborationType, CollaborationTypeAdmin)
admin.site.register(Region, RegionAdmin)
@admin.register(Organization)
class OrganisationAdmin(admin.ModelAdmin):
     list_display = ('ref','type','narrative','discriminator')
     search_fields = ('ref','type','narrative')
     list_filter = ('ref','type','narrative')
     list_per_page=10
     inlines = [
       Contactline
    ]


admin.site.register(Sector, SectorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(DefaultAidType, DefaultAidTypeAdmin)
admin.site.register(DefaultFinanceType, DefaultFinanceTypeAdmin)
admin.site.register(HumanitarianScope, HumanitarianScopeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Period)
admin.site.register(Comment)
admin.site.register(Dimension)
admin.site.register(DocumentLink)
admin.site.register(ContactInfo)
