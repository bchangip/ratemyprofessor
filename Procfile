release: python manage.py migrate
web: python src/manage.py test; gunicorn ratemyprofessor.wsgi --log-file -
