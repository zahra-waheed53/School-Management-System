from django.db import models
from django.contrib.auth.models import AbstractUser

from api.models import Section


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    def __str__(self):
        return self.username


class Student(models.Model):
    section = models.ForeignKey('api.Section', on_delete=models.CASCADE, related_name="student")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendance = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    attendance = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
    attendance = models.IntegerField(default=0)
    designation = models.CharField(max_length=100, default="teacher")
    section = models.ManyToManyField('api.Section',through='api.Subject', related_name="section_teachers", blank=True)
    def __str__(self):
        return self.user.username

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Section, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
