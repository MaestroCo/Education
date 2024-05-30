from .models import CoursesModel, TeachersModel, StudentsModel
from rest_framework import serializers


# class CoursesSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=75)
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     duration = serializers.IntegerField(min_value=0)
#
#     def create(self, validated_data):
#         return CoursesModel.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.price = validated_data.get('price', instance.price)
#         instance.duration = validated_data.get('duration', instance.duration)
#         instance.save()
#         return instance
class CoursesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    duration = serializers.IntegerField(min_value=0)

    def create(self, validated_data):
        return CoursesModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance

    def get_total_price(self, obj):
        return obj.calculate_total_price()

    def to_representation(self, instance):
        representation = super(CoursesSerializer, self).to_representation(instance)
        representation['total_price'] = self.get_total_price(instance)
        return representation

class TeachersSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
    experience = serializers.CharField(max_length=50)
    courses_id = serializers.IntegerField()

    def create(self, validated_data):
        return TeachersModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.status = validated_data.get('status', instance.status)
        instance.experience = validated_data.get('experience', instance.experience)
        instance.courses_id = validated_data.get('courses_id', instance.courses_id)
        instance.save()
        return instance


class StudentsSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.IntegerField()
    parents_phone = serializers.IntegerField()
    telegram_link = serializers.CharField()
    address = serializers.CharField()
    courses_id = serializers.IntegerField()
    teachers_id = serializers.IntegerField()

    def create(self, validated_data):
        return StudentsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.telegram_link = validated_data.get('telegram_link', instance.telegram_link)
        instance.address = validated_data.get('address', instance.address)
        instance.courses_id = validated_data.get('courses_id', instance.courses_id)
        instance.teachers_id = validated_data.get('teachers_id', instance.teachers_id)
        instance.save()
        return instance
