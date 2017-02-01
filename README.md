## CMS portal for main website of IITG

### How to install

```
    $ git clone https://github.com/rohanaggarwal7997/IITG-CMS.git
    $ cd into the folder
    $ virtualenv swciitg
    $ source swciitg/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
```
