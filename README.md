# How to run

1. `pip install -r requirements.txt` installs the required packages, including Django
2. `cd mysite`
3. `./manage.py migrate` will create and update the SQLite database
4. `./manage.py createsuperuser` will create an admin user
5. `./manage.py runserver` will serve up the app on http://localhost:8000/birthday
