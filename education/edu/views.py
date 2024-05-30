from django.shortcuts import render
from .models import CoursesModel, TeachersModel, StudentsModel
from .serializers import StudentsSerializer, TeachersSerializer, CoursesSerializer
from rest_framework import generics, mixins, permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user and request.user.is_staff


class StudentsView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, mixins.DestroyModelMixin):

    queryset = StudentsModel.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [CustomPermission]

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CoursesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = CoursesModel.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [CustomPermission]

    def get_queryset(self):
        queryset = CoursesModel.objects.all()
        for course in queryset:
            course.total_price = course.calculate_total_price()
        return queryset

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TeachersView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                   mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = TeachersModel.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [CustomPermission]

    def get(self, request, *args, **kwargs):
        if 'pk' in self.kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
