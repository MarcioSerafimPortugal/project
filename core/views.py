from django.shortcuts import render
from core.models import Project
from core.models import ResultProject

def load(request):
    load_project = Project.objects.all()
    data = {
        'load': load_project
    }
    return render(request, 'load.html', data)
 
def form(request):
    return render(request, 'form.html')

def result(request):
    ResultProject.objects.create(
        pspent = request.POST['pspent'],
        espent = request.POST['espent'],
        mspent = request.POST['mspent'],
    )
    return render(request, 'result.html')