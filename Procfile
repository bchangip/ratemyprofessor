release: python manage.py migrate
web: python manage.py test; gunicorn ratemyprofessor.wsgi --log-file -
