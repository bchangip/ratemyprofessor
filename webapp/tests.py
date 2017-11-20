from django.test import TestCase
from .models import Student, StudentForm, Review, ReviewForm, Course, CourseForm, Professor, ProfessorForm, ReviewLike

# Create your tests here.

class StudentTestCase(TestCase):
	def setUp(self):
		Student.objects.create(
			username="test",
			firstname="test",
			lastname="test",
			email="test",
			career="test",
			interest1="test",
			interest2="test",
			interest3="test",
			highschool="test"
		)

		Student.objects.create(
			username="test2",
			firstname="test2",
			lastname="test2",
			email="test2",
			career="test2",
			interest1="test2",
			interest2="test2",
			interest3="test2",
			highschool="test2"
		)

		print("Doing things")
	def testStudents(self):
		test = Student.objects.get(username="test")
		anotherTest = Student.objects.get(username="test2")

		self.assertEqual(test.username, 'test')
		print("Testing things")

	def testStudents2(self):
		test = Student.objects.get(username="test")
		anotherTest = Student.objects.get(username="test2")

		self.assertEqual(test.username, 'test')
		print("Testing things")