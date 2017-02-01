from django.utils import timezone
from django.db import models


# Create your models here.


class Events(models.Model):
    """
    The Events and Happenings model
    :fields:
        * Title : The title of the event
        * date : The date of the event
        * image_url : The url of the image inside the event
        * description : The description of the event
        * link : The link of the event/ What the event Redirects to

    :Functions:
        * __unicode__ : Returns the Event title of calling the python object.
    """
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    image_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    link = models.URLField()

    def __unicode__(self):
        return self.title


class Achievements(models.Model):
    """
    The achivements model
    fields:
    title : the title of the achievement
    description : description of the achievement
    imageurl:link for the image
    link: url for the main achievement
    date:date of the achievement

    """
    title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    image_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    link = models.URLField()

    def __unicode__(self):
        return self.title


class News(models.Model):
    """
    The News model
    fields:
    description : description of the event
    link: url for the main event
    date:date of the event

    """
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=1000)
    link = models.URLField()

    def __unicode__(self):
        return self.description

class ddesk(models.Model):
    """
    The director's desk model
    fields:
    image url: url of image
    description: What our esteemed director wants to tell us
    """
    description = models.CharField(max_length=1000)
    link = models.URLField()
    id = models.IntegerField(primary_key=True)          #while creating database initialize only one object with pk=1

    def __unicode__(self):
        return self.description

class initiatives(models.Model):
    """
       The achivements model
       fields:
       imageurl : the imageurl
       description : description of the initiative
       link: url for the main initiative

       """

    image_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    link = models.URLField()

    def __unicode__(self):
        return self.title
