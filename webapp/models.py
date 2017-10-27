from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
import django.contrib.postgres.fields as postgresModule

# Create your models here.

class Student(models.Model):
	username = models.CharField(max_length=10)
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)
	email = models.EmailField()
	career = models.CharField(max_length=40)
	interest1 = models.CharField(max_length=10, blank=True)
	interest2 = models.CharField(max_length=10, blank=True)
	interest3 = models.CharField(max_length=10, blank=True)
	highschool = models.CharField(max_length=40)

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['firstname', 'lastname', 'email', 'career', 'interest1', 'interest2', 'interest3', 'highschool']
	
class Course(models.Model):
	name = models.CharField(max_length=20)

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name']

class Professor(models.Model):
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)

class ProfessorForm(ModelForm):
	class Meta:
		model = Professor
		fields = ['firstname', 'lastname']

class Review(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
	idProfessor = models.ManyToManyField(Professor, on_delete=models.CASCADE)
	rating = models.IntegerField()
	comment = models.CharField(max_length=300)

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['idCourse', 'idProfessor', 'rating', 'comment']

class ReviewLike(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idReview = models.ForeignKey(Review, on_delete=models.CASCADE)
	liked = models.BooleanField()

class ProfessorLike(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
	liked = models.BooleanField()
