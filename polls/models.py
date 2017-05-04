from django.db import models
from django.contrib import auth  # for the password/authentication system


class User(models.Model):
    """
    Class to describe a user.
    """
    # TODO: hashed passwords https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
    first_name = models.TextField('First Name')
    last_name = models.TextField('Last Name')
    email = models.EmailField('Email Address')
    date_of_birth = models.DateField('Date of Birth')


class Funeral(models.Model):
    """
    Class to describe a funeral.
    Funerals must be linked to a user
    """
    #deceased = models.ForeignKey(User, 'The User whose funeral is being planned')
    date = models.DateField('Date of the Funeral')
    type = models.TextField('Type of Burial')
    location = models.TextField('Location')
    tombstone = models.BooleanField('Tombstone wanted?')
    layed_out = models.BooleanField('User wants to be layed out?')
    additional_comments = models.TextField('Additional Comments')


class Optionals(models.Model):
    cheer = models.TextField('Words of Cheer')
    guest_list = models.TextField('Guest List (json)')
