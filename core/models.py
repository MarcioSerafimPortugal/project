from django.db import models
from django.contrib.auth.models import User


class ProjectName(models.Model):
    project_name = models.CharField(max_length=30)

    def __str__(self):
        return self.project_name


class ProjectMonth(models.Model):
    project_month = models.CharField(max_length=30)

    def __str__(self):
        return self.project_month


DEFAULT_ProjectName_project_name = 1
DEFAULT_ProjectMonth_project_month = 1
class Project(models.Model):
    project = models.ForeignKey(ProjectName, on_delete=models.SET_NULL, null=True, verbose_name='Project:', default=1)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Employee:', default=1)
    month = models.ForeignKey(ProjectMonth, on_delete=models.SET_NULL, null=True, verbose_name='Month:', default=1)
    date = models.DateField(verbose_name='Date:')
    hours = models.DurationField(verbose_name='Hours:')
    activity = models.TextField(verbose_name='Activity:')

    def __str__(self):
        return self.project
        
    def __str__(self):
        return self.project.project_name
        return self.month.project_month


class ResultProject(models.Model):
    pspent = models.CharField(max_length=30, verbose_name='Project')
    espent = models.CharField(max_length=30, verbose_name='Employee')
    mspent = models.CharField(max_length=30, verbose_name='Month')
    tspent = models.DurationField(verbose_name='Total Hour Spent:', null=True, blank=True)
    
    def __str__(self):
        return self.pspent
