from django.contrib import admin

from project.models import Project
from .models import Project, Department

admin.site.register(Project),
admin.site.register(Department),
