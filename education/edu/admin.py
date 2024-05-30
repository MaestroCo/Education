from django.contrib import admin
from .models import TeachersModel, CoursesModel, StudentsModel

admin.site.register(TeachersModel)
admin.site.register(CoursesModel)
admin.site.register(StudentsModel)
