from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import registration.signals
from models import Student, StudentForm, Review, ReviewForm, Course, CourseForm, Professor, ProfessorForm
from django.forms import modelformset_factory
import time

# Create connection with postgres DB
import psycopg2

try:
    conn = psycopg2.connect("dbname='ratemyprofessor' user='bchangip' host='localhost' password='bchangip'")
    conn.autocommit = True;
except:
	continue
    # print "Connection to DB failed."

cur = conn.cursor();

# cur.execute('''INSERT INTO student VALUES (1, 'bchangip', 'Bryan', 'Chan', 'xchangip@gmail.com', 'compu', ARRAY['Progra', 'Musica'], 'Bressani')''')
# # print("Performing SELECT")
# cur.execute('''SELECT firstname FROM student;''')
# rows = cur.fetchall()
# # print rows



# Create your views here.
def homepage(request):
	return render(request, 'webapp/homepage.html')

@login_required
def profilePage(request):
	studentData = Student.objects.get(pk=request.user.id)
	if(request.method == 'GET'):
		# # print(StudentForm(instance=studentData))
		# print(ReviewForm())

		return render(
			request,
			'webapp/profile.html',
			{
				'username': studentData.username,
				'firstname': studentData.firstname,
				'lastname': studentData.lastname,
				'email': studentData.email,
				'career': studentData.career,
				'interest1': studentData.interest1,
				'interest2': studentData.interest2,
				'interest3': studentData.interest3,
				'highschool': studentData.highschool,
				'editProfileForm': StudentForm(instance=studentData),
				'addReviewForm': ReviewForm()
			}
		)
	else:
		studentData = StudentForm(request.POST)
		if studentData.is_valid():
			studentData.save()
			# print("Perfil actualizado.")

		studentData = Student.objects.get(pk=request.user.id)
		return render(
			request,
			'webapp/profile.html',
			{
				'username': studentData.username,
				'firstname': studentData.firstname,
				'lastname': studentData.lastname,
				'email': studentData.email,
				'career': studentData.career,
				'interest1': studentData.interest1,
				'interest2': studentData.interest2,
				'interest3': studentData.interest3,
				'highschool': studentData.highschool,
				'editProfileForm': StudentForm(instance=studentData)
			}
		)

@login_required
def addPage(request):
	return render(request, 'webapp/add.html')

@login_required
def addProfesorPage(request):
	if(request.method == 'GET'):
		return render(
			request, 
			'webapp/addProfesor.html',
			{
				'addProfessorForm': ProfessorForm()
			}
		)
	else:
		newProfessor = ProfessorForm(request.POST)
		if newProfessor.is_valid():
			newProfessor.save()
		return render(
			request, 
			'webapp/addProfesor.html',
			{
				'addProfessorForm': ProfessorForm()
			}
		)


@login_required
def professorSearchPage(request):
	if(request.method == 'GET'):
		return render(
			request,
			'webapp/professorSearch.html',
			{
				'professorSearchForm': ProfessorForm()
			}
		)
	else:
		query = ProfessorForm(request.POST)
		if query.is_valid():
			# Extract non empty fields and search
			# print "Query professor"
			# print request.POST['firstname']
			# print request.POST['lastname']
			print Professor.objects.filter(
				firstname__icontains=request.POST['firstname'], 
				lastname__icontains=request.POST['lastname']
			)
			return render(request, 'webapp/professorSearchResults.html')	
	return render(request, 'webapp/professorSearch.html')

@login_required
def addCoursePage(request):
	if(request.method == 'GET'):
		return render(
			request, 
			'webapp/addCourse.html',
			{
				'addCourseForm': CourseForm()
			}
		)
	else:
		newCourse = CourseForm(request.POST)
		if newCourse.is_valid():
			newCourse.save()
		return render(
			request, 
			'webapp/addCourse.html',
			{
				'addCourseForm': CourseForm()
			}
		)

@login_required
def courseSearchPage(request):
	if(request.method == 'GET'):
		return render(
			request,
			'webapp/courseSearch.html',
			{
				'courseSearchForm': CourseForm()
			}
		)
	else:
		query = CourseForm(request.POST)
		if query.is_valid():
			# Extract non empty fields and search
			# print "Query course: "
			# print request.POST['name']
			return render(request, 'webapp/courseSearchResults.html')	
		return render(request, 'webapp/courseSearch.html')

@login_required
def addReviewPage(request):
	if(request.method == 'GET'):
		return render(
			request, 
			'webapp/addReview.html',
			{
				'addReviewForm': ReviewForm()
			}
		)
	else:
		newReview = ReviewForm(request.POST)
		if newReview.is_valid():
			newReview.save()
		return render(
			request, 
			'webapp/addReview.html',
			{
				'addReviewForm': ReviewForm()
			}
		)


@login_required
def searchPage(request):
	return render(request, 'webapp/search.html')

@login_required
def highSchoolRecommendedProfessorsPage(request):
	return render(request, 'webapp/highSchoolRecommendedProfessors.html')

@login_required
def highSchoolRecommendedCoursesPage(request):
	return render(request, 'webapp/highSchoolRecommendedCourses.html')

@login_required
def interestsRecommendedProfessorsPage(request):
	return render(request, 'webapp/interestsRecommendedProfessors.html')

@login_required
def interestsRecommendedCoursesPage(request):
	return render(request, 'webapp/interestsRecommendedCourses.html')

def jsonPage(request):
	query = request.GET.get('query', '')
	suggestionSize = request.GET.get('suggestionSize', '')

	# print("Query: "+query)
	# print("Suggestion Size: "+suggestionSize)

	time.sleep(0.5)


	return JsonResponse([{'id': 0, 'name': 'Bryan'}, {'id': 1, 'name': 'Michael'}, {'id': 2, 'name': 'Emily'}], safe=False)

#Signals
from django.core.signals import request_finished
from django.dispatch import receiver

# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     # print("Request finished!")

@receiver(registration.signals.user_registered)
def userRegistered(sender, user, request, **kwargs):
	#Create entry in users table
	# cur.execute("INSERT INTO student VALUES ("+str(user.id)+", '"+str(user.username)+"', '', '', '"+str(user.email)+"', '', ARRAY[]::VARCHAR(15)[], '')")

	#Create user on Student model
	tempStudent = Student(pk=user.id, username=user.username, email=user.email)
	tempStudent.save()

	# print "A new user registered, with id:"+str(user.id)+" username:"+str(user.username)+" email:"+str(user.email)
