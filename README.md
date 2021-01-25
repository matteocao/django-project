# django-project
A Webapp for ML computations.

# Installation

Go to the folder where you want to start creating your project.

Create conda environment, e.g. via
```
conda create -n djangoenv python=3.8
```

Then activate it with
```
conda activate djangoenv
```

Install the requirements in the nevironment via
```
pip install -r requirements.txt
```

Finally, set the up the new project with
```
django-admin startproject mysite
```
In the newly created folder, you will find the following files:

 - `settings.py` a file containing the generic settings of the project
 - `urls.py` a file containing the urls of the apps of the project
 - `wsgi.py` a file for the WSGI deployment
 
# To make the app work
 
## Run django server
Go inside the outer `gtdainterface` folder and then run:
```
python manage.py runserver 8080
```

## Run Redis server
Just type
```
redis-server
```

## Run Redis-RQ
Go inside the outer `gtdainterface` folder and then run:
```
python manage.py rqworker default
```

# Create an app

Go inside the outer `mysite` folder, and then choose the name -- `polls` in this case -- and run
```
python manage.py startapp polls
```
## Inside the newly created app folder you will find:

- `views.py` this file is to define the classes or functions associated to the views (basically, the get response). Each function must return the `httpResponse` 
- `admin.py` is the file to improve the admin view
- `models.py` is teh file with the definition of the classes associated to the database structures
- `tests.py` is for the unit and integration tests
- `urls.py` specifies all the urls associated to the views
- `apps.py` a file with the app configurations

# Create tables in DB
To create tables in the databse for auth, session, contenttype, messages, staticfiles write
```
python manage.py migrate
```

# Migrating new model

If you create a new DB model, then *add* its migration via
```
python manage.py makemigrations polls
```
If you are using postgreSQL, then use
```
python manage.py sqlmigrate polls 0001
```
To actually *apply the model tables* in your database, use
```
python manage.py migrate
```
# Django Python interactive interface

To open up the Python shell use
```
python manage.py shell
```
# Create admin user

Just type
```
python manage.py createsuperuser
```
E.G. admin, admin@example.com, admin

# Run tests

To run the tests, that you can write in the `polls/tests.py` file, write
```
python manage.py test polls
```

# Run Redis server

Forr ML ocmputation, it is better to have a Redis server that enqueues the jobs and execute them in the background.

Install `Redis` and Python `rq`:
```
brew install redis
pip install django-rq
```
To star the redis server, run 
```
redis-server
```
Once you are done, follow the instructions of [django-rq](https://github.com/rq/django-rq). Then  run the workers with:
```
python manage.py rqworker default
```
You can also add the  `high` and `low` queues

# Use signals
You can use signals that are triggered when a certain event happens. For exammple, every time an entry is saved in a table of the database.

To do so, initalise the connections in the `apps.py` file and then create a new `signals.py` module with the receiver functions.
