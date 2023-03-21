from django.contrib import admin

from homework62.models import Issue, Project, Status, Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('summary', 'status', 'created_date')
    list_filter = ('status', 'type')
    search_fields = ('summary', 'description')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Issue, IssueAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
