from django.shortcuts import render
from portfolio.models import Project
# Create your views here.
def portfolio_records_views(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})
