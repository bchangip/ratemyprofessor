from __future__ import unicode_literals

from django.db import models
import django.contrib.postgres.fields as postgresModule

# Create your models here.

class Student(models.Model):
	username = models.CharField(max_length=10)
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)
	email = models.EmailField()
	career = models.CharField(max_length=40)
	interests = postgresModule.ArrayField(
		models.CharField(max_length=10, blank=True)
	)
	highschool = models.CharField(max_length=40)
	
class Course(models.Model):
	name = models.CharField(max_length=20)

class Professor(models.Model):
	firstname = models.CharField(max_length=10)
	lastname = models.CharField(max_length=10)

class Review(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
	idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
	rating = models.IntegerField()
	comment = models.CharField(max_length=300)

class ReviewLike(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idReview = models.ForeignKey(Review, on_delete=models.CASCADE)
	liked = models.BooleanField()

class ProfessorLike(models.Model):
	idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
	idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
	liked = models.BooleanField()
