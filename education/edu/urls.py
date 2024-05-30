from .views import TeachersView, StudentsView, CoursesView
from django.urls import path

urlpatterns = [
    path('students/api/v1/', StudentsView.as_view()),
    path('students/api/v1/<int:pk>', StudentsView.as_view()),

    path('teachers/api/v2/', TeachersView.as_view()),
    path('teachers/api/v2/<int:pk>', TeachersView.as_view()),

    path('courses/api/v3/', CoursesView.as_view()),
    path('courses/api/v3/<int:pk>', CoursesView.as_view()),
]