from django.contrib import admin



from iati_activities.models import Activity,ActivityCollaborationType,ActivityDate,ActivityHumanitarianScope, \
    ActivityLocation, ActivityOrganization, ActivityParticipatingOrg, ActivitySector, ActivityTag, ActualDimension, \
        Actual, ActualDocumentLink, Baseline, Budget, BaselineDocumentLink, Comment, ConditionActivity, \
        ContactInfo, Dimension, DocumentLink, DocumentLinkIndicator, DocumentLinkResults, Indicator, Period, PlannedDisbursement,  \
            Results, Target, TargetComment2, TargetDimension, Transaction, TransactionSector

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

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [
        ActivityLocationline, ActivitySectorline, ActivityOrganizationline, Budgetline, ActivityTagline, ActivityParticipatingOrgline, ActivityDateline,\
             Resultsline, ActivityCollaborationTypeline, ActivityHumanitarianScopeline, ConditionActivityline
    ]

admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    inlines = [
        TransactionSector, 
    ]