from django.shortcuts import render
from django.http import HttpResponse



project = [
    {
    'project_name': 'Students System for Managing Projects',
    'department': 'Systems',
    'qulification': 'Bacholar',
    'min_student': '3',
    'max_student': '5',
    'project_year': '2022',
    },

    {
    'project_name': 'Sales Points',
    'department': 'Web',
    'qulification': 'Bacholar',
    'min_student': '3',
    'max_student': '5',
    'project_year': '2022',
    }
]

def home(request):
    context = {
        'project': project
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
