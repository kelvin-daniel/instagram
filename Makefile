runs:
	./manage.py runserver

check:
	./manage.py check

test:
	coverage run ./manage.py test
	
superuser:
	./manage.py createsuperuser --username $(name)

collectstatic:
	./manage.py collectstatic

migrations:
	./manage.py makemigrations 

migrate:
	./manage.py migrate

start:
	django-admin startapp $(name)

report:
	coverage html