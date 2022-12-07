from django.contrib import admin


from iati_referentiel.models import CollaborationType, Country, DefaultAidType, DefaultFinanceType, \
HumanitarianScope, Location, Organization, Region, Sector, Tag, Condition

class CollaborationTypeAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)

class CountryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('regionid','code','name','discriminator')
    search_fields = ('regionid','code','name')
    list_filter = ('regionid','code','name')

class DefaultAidTypeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)

class DefaultFinanceTypeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)
    list_filter = ('code',)

class HumanitarianScopeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)
    list_filter = ('type',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('countryid3','ref','location_reach','code','name','description','activity_location','administrative_code','administrative_level','pos','location_class')
    search_fields = ('countryid3','ref','location_reach','code','name')
    list_filter = ('countryid3','ref','location_reach','code','name')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('ref','type','narrative','discriminator')
    search_fields = ('ref','type','narrative')
    list_filter = ('ref','type','narrative')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('continent','name','discriminator')
    search_fields = ('continent','name')
    list_filter = ('continent','name')

class SectorAdmin(admin.ModelAdmin):
    list_display = ('code','percentage','narrative')
    search_fields = ('code',)
    list_filter = ('code',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('code','narrative')
    search_fields = ('code',)
    list_filter = ('code',)

class ConditionAdmin(admin.ModelAdmin):
    list_display = ('attached','condition','type')
    search_fields = ('condition', 'type')
    list_filter = ('attached',)


admin.site.register(CollaborationType, CollaborationTypeAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(DefaultAidType, DefaultAidTypeAdmin)
admin.site.register(DefaultFinanceType, DefaultFinanceTypeAdmin)
admin.site.register(HumanitarianScope, HumanitarianScopeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Condition, ConditionAdmin)