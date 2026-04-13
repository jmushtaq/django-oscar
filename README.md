# Setup

https://django-oscar.readthedocs.io/en/latest/internals/sandbox.html#run-the-sandbox-locally

```
$ git clone https://github.com/django-oscar/django-oscar.git
$ cd django-oscar
$ mkvirtualenv --python=python3 oscar  # needs virtualenvwrapper

# Needed (JM)
python3.12 -m pip install setuptools

(oscar) $ make sandbox
(oscar) $ sandbox/manage.py runserver
```

# Theme changer
http://localhost:8000/dashboard/themes/

