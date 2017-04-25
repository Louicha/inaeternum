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


class Funeral(models.Model):
    """
    Class to describe a funeral.
    Funerals must be linked to a user
    """
    deceased = models.ForeignKey(User, 'The User whose funeral is being planned')
    date = models.DateField('Date of the Funeral')
    additional_comments = models.TextField('Additional Comments')
