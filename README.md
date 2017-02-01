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
``` $ For making the director desk work , initialize one entry in the database with primary key 1 (important or 404 not found will come)
        It is registered on admin section.
