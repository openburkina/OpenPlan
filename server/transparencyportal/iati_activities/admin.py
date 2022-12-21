from django.contrib import admin



from iati_activities.models import Activity,ActivityCollaborationType,ActivityDate,ActivityHumanitarianScope, \
    ActivityLocation, ActivityOrganization, ActivityParticipatingOrg, ActivitySector, ActivityTag, ActualDimension, \
        Actual, ActualDocumentLink, Baseline, Budget, BaselineDocumentLink, Comment, ConditionActivity, \
        ContactInfo, Dimension, DocumentLink, DocumentLinkIndicator, DocumentLinkResults, Indicator, Period, PlannedDisbursement,  \
        Results, Target, TargetComment2, TargetDimension, Transaction, TransactionSector,DefaultAidTypeActivity, \
        DefaultFinanceTypeActivity


class Actualline(admin.StackedInline):
    model = Actual

class ActualDocumentLinkline(admin.StackedInline):
    model = ActualDocumentLink

class Baselineline(admin.StackedInline):
    model = Baseline

class BaselineDocumentLinkline(admin.StackedInline):
    model = BaselineDocumentLink

class Commentline(admin.StackedInline):
    model = Comment

class ActualDimensionline(admin.StackedInline):
    model = ActualDimension

class Dimensionline(admin.StackedInline):
    model = Dimension

class DocumentLinkline(admin.StackedInline):
    model = DocumentLink

class DocumentLinkIndicatorline(admin.StackedInline):
    model = DocumentLinkIndicator

class DocumentLinkResultsline(admin.StackedInline):
    model = DocumentLinkResults

class Indicatorline(admin.StackedInline):
    model = Indicator

class Periodline(admin.StackedInline):
    model = Period

class Targetline(admin.StackedInline):
    model = Target

class PlannedDisbursementline(admin.StackedInline):
    model = PlannedDisbursement

class TargetComment2line(admin.StackedInline):
    model = TargetComment2

class TargetDimensionline(admin.StackedInline):
    model = TargetDimension

class DefaultAidTypeActivityline(admin.StackedInline):
    model = DefaultAidTypeActivity

class DefaultFinanceTypeActivityline(admin.StackedInline):
    model = DefaultFinanceTypeActivity

class ActivityCollaborationTypeline(admin.StackedInline):
    model = ActivityCollaborationType

class ActivityHumanitarianScopeline(admin.StackedInline):
    model = ActivityHumanitarianScope

class ActivityParticipatingOrgline(admin.StackedInline):
    model = ActivityParticipatingOrg

class ActivitySectorline(admin.StackedInline):
    model = ActivitySector

class ActivityDateline(admin.StackedInline):
    model = ActivityDate

class ActivityLocationline(admin.StackedInline):
    model = ActivityLocation

class Resultsline(admin.StackedInline):
    model = Results


class ActivityOrganizationline(admin.StackedInline):
    model = ActivityOrganization

class ActivityTagline(admin.StackedInline):
    model = ActivityTag

class Budgetline(admin.StackedInline):
    model = Budget

class ConditionActivityline(admin.StackedInline):
    model = ConditionActivity

class TransactionSectorline(admin.StackedInline):
    model = TransactionSector

class Transactionline(admin.StackedInline):
    model = Transaction

class Contactline(admin.StackedInline):
    model = ContactInfo

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('iati_identifier','title','regionid3','countryid3','humanitarian')
    search_fields = ('regionid3','countryid3','iati_identifier')
    list_filter = ('humanitarian','regionid3','countryid3','iati_identifier')
    inlines = [
        ActivityLocationline, ActivitySectorline, ActivityOrganizationline, Budgetline, ActivityTagline, ActivityParticipatingOrgline, ActivityDateline,\
             Transactionline, Resultsline, ActivityCollaborationTypeline, ActivityHumanitarianScopeline, ConditionActivityline, DefaultFinanceTypeActivityline, \
                DefaultAidTypeActivityline, DocumentLinkline, PlannedDisbursementline
    ]

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('measure','title','description','code','ascending')
    search_fields = ('measure','title')
    list_filter = ('measure','title','code','ascending')
    inlines = [
        Periodline, DocumentLinkIndicatorline,Baselineline
    ]

@admin.register(Target)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('locationid','value','periodid')
    search_fields = ('locationid','value')
    list_filter = ('locationid','value')
    inlines = [
        TargetComment2line, TargetDimensionline
    ]

@admin.register(Actual)
class ActualAdmin(admin.ModelAdmin):
    list_display = ('value','periodid')
    search_fields = ('periodid','value')
    list_filter = ('periodid','value')
    inlines = [
        ActualDimensionline, ActualDocumentLinkline
    ]

""" class ActualAdmin(admin.ModelAdmin):
    pass

class ActualDocumentLinkAdmin(admin.ModelAdmin):
    pass

class Baselineline(admin.ModelAdmin):
    pass

class BaselineDocumentLinkAdmin(admin.ModelAdmin):
    pass

class Commentline(admin.ModelAdmin):
    pass

class ActualDimensionAdmin(admin.ModelAdmin):
    pass

class Dimensionline(admin.ModelAdmin):
    pass

class DocumentLinkline(admin.ModelAdmin):
    pass

class DocumentLinkIndicatorline(admin.ModelAdmin):
    pass

class DocumentLinkResultsline(admin.ModelAdmin):
    pass

class Indicatorline(admin.ModelAdmin):
    pass

class Periodline(admin.ModelAdmin):
    pass

class Targetline(admin.ModelAdmin):
    pass

class PlannedDisbursementline(admin.ModelAdmin):
    pass

class TargetComment2line(admin.ModelAdmin):
    pass

class TargetDimension3line(admin.ModelAdmin):
    pass

class DefaultAidTypeActivityline(admin.ModelAdmin):
    pass

class DefaultFinanceTypeActivityline(admin.ModelAdmin):
    pass

class ActivityCollaborationTypeline(admin.ModelAdmin):
    pass

class ActivityHumanitarianScopeline(admin.ModelAdmin):
    pass

class ActivityParticipatingOrgline(admin.ModelAdmin):
    pass

class ActivitySectorline(admin.ModelAdmin):
    pass

class ActivityDateline(admin.ModelAdmin):
    pass

class ActivityLocationline(admin.ModelAdmin):
    pass

class Resultsline(admin.ModelAdmin):
    pass

class ActivityOrganizationline(admin.ModelAdmin):
    pass

class ActivityTagline(admin.ModelAdmin):
    pass

class Budgetline(admin.ModelAdmin):
    pass

class ConditionActivityline(admin.ModelAdmin):
    pass

class TransactionSectorline(admin.ModelAdmin):
    pass

class Transactionline(admin.ModelAdmin):
    pass

class Contactline(admin.ModelAdmin):
    pass
 """