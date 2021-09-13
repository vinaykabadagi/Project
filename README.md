# Project
Prerequisites
1. Install Python
Install python-3.7.2 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

2. Install Django
```bash
py -m pip install Django
```
3. Install MongoDB <br>
https://docs.mongodb.com/manual/installation/

4. Install Djongo
```bash
py pip install djongo
```
# Edit project settings(settings.py)
```bash
# Edit Database configurations with your MongoDB configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ott',
    }
}
```

# Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Create Super User
python manage.py createsuperuser

# Run the server
python manage.py runserver 
```
Try opening http://localhost:8000 in the browser. Now you are good to go.
