from django.contrib import admin
from django.contrib.auth.models import User
from core.models import ProjectName, ProjectMonth, Project
from core.models import ResultProject
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget


class ProjectResources(resources.ModelResource):
    employee = fields.Field(
        column_name='employee',
        attribute='employee',
        widget=ForeignKeyWidget(User, 'username'))
    project = fields.Field(
        column_name='project',
        attribute='project',
        widget=ForeignKeyWidget(ProjectName, 'project_name'))
    mouth = fields.Field(
        column_name='mouth',
        attribute='mouth',
        widget=ForeignKeyWidget(ProjectMonth, 'project_mouth'))

    class Meta:
        model = Project
        fields = ('employee', 'project', 'date', 'hours', 'activity')


class ProjectAdmin(ImportExportModelAdmin):
    resource_class =  ProjectResources
    list_display = ['employee', 'project', 'month', 'date', 'hours', 'activity']
    list_filter = ['employee', 'project', 'month']

    def complete_name(self, obj):
        return obj.employee.get_full_name()


class ResultProjectAdmin(ImportExportModelAdmin):
    list_display = ['pspent', 'espent', 'mspent', 'tspent']
    search_fields = ['pspent', 'espent', 'mspent']
    list_filter = ['pspent', 'espent', 'mspent']
    exclude = ['tspent']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ResultProject, ResultProjectAdmin)
