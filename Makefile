mig:
	python3 manage.py makemigrations
	python3 manage.py migrate
unmig:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
remig:
    python3 manage.py remig