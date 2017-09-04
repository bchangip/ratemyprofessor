from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import registration.signals

# Create connection with postgres DB
import psycopg2

try:
    conn = psycopg2.connect("dbname='ratemyprofessor' user='bchangip' host='localhost' password='bchangip'")
    conn.autocommit = True;
except:
    print "Connection to DB failed."

cur = conn.cursor();

# cur.execute('''INSERT INTO student VALUES (1, 'bchangip', 'Bryan', 'Chan', 'xchangip@gmail.com', 'compu', ARRAY['Progra', 'Musica'], 'Bressani')''')
# print("Performing SELECT")
# cur.execute('''SELECT firstname FROM student;''')
# rows = cur.fetchall()
# print rows



# Create your views here.
def homepage(request):
	return render(request, 'webapp/homepage.html')

@login_required
def profilePage(request):
	'''
	id INT,
	username VARCHAR(10),
	firstname VARCHAR(10),
	lastname VARCHAR(10),
	email VARCHAR(40),
	career VARCHAR(40),
	interests VARCHAR(15)[],
	highschool VARCHAR(40),
	'''
	print("Performing SELECT with user:")
	for info in request.user:
		print info
	cur.execute('''SELECT * FROM student WHERE username='bchangip';''')
	result = cur.fetchone()
	if(result is not None):
		id, username, firstname, lastname, email, career, interests, highschool = result
		# print username

	# print(rows[0][1])
	# print rows

	return render(request, 'webapp/profile.html')

@login_required
def addPage(request):
	return render(request, 'webapp/add.html')

@login_required
def addProfesorPage(request):
	return render(request, 'webapp/addProfesor.html')

@login_required
def addCoursePage(request):
	return render(request, 'webapp/addCourse.html')


@login_required
def searchPage(request):
	return render(request, 'webapp/search.html')

@login_required
def professorSearchPage(request):
	return render(request, 'webapp/professorSearch.html')

@login_required
def courseSearchPage(request):
	return render(request, 'webapp/courseSearch.html')

@login_required
def loginTest(request):
	return HttpResponse("You shouldnt see this.")

#Signals
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")

@receiver(registration.signals.user_registered)
def userRegistered(sender, user, request, **kwargs):
	#Create entry in users table
	cur.execute("INSERT INTO student VALUES ("+str(user.id)+", '"+str(user.username)+"', '', '', '"+str(user.email)+"', '', ARRAY[]::VARCHAR(15)[], '')")

	print "A new user registered, with id:"+str(user.id)+" username:"+str(user.username)+" email:"+str(user.email)