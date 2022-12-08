from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

projectsList =[
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description': 'Fully functional ecommerce Website'
    },
    {
        'id':'2',
        'title':'Protofolio  Website',
        'description': 'This was a project where i build out my portofolio'
    },
    {
        'id':'3',
        'title':'Social  Website',
        'description': 'Awesome open source project i am still working'
    },
]

def projects(request):
    msg = "project"
    number = 10
    context = {
        'msg': msg,
        'number': number,
        'projects': projectsList,
        }
    return render(request, 'projects/projects.html', context )

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] ==pk :
            projectObj = i
    return render(request, 'projects/single-projects.html', {'project': projectObj})

