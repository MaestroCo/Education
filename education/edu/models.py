from django.db import models


class CoursesModel(models.Model):
    name = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()

    def __str__(self):
        return self.name

    def calculate_total_price(self):
        return self.price * self.duration


class TeachersModel(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    courses = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class StudentsModel(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    parents_phone = models.IntegerField()
    telegram_link = models.TextField()
    address = models.TextField()
    courses = models.ForeignKey(CoursesModel, on_delete=models.CASCADE)
    teachers = models.ForeignKey(TeachersModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


