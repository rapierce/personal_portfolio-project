from django.shortcuts import render, get_object_or_404
from .models import project

def home(request):
    projects = project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def portfolio_Project_Detail(request, portfolio_Project_Id):
    one_Project = get_object_or_404(project, pk=portfolio_Project_Id)
    return render(request, 'portfolio/portfolio_Project_Detail.html', {'one_Project':one_Project})


    # return render(request, 'portfolio/portfolio_Project_Detail.html', {'id':portfolio_Project_Id}) 