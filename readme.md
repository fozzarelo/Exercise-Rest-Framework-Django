
## Requires: 
	
	Python
	Pip
	Postgresql
	
## Steps:
	
Copy in folder

Setup virtual environment:
	
	-> virtualenv virtual
	-> source virtual/bin/activate
	-> pip install -r requirements.txt
	-> deactivate
	
Setup database:

	-> createdb dbname
	Modify db in settings.py to your own dbname, username and password.
	-> python manage.py migrate
	
Run server
	-> python manage.py runserver
