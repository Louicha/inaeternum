from django.db import models
from django.contrib import auth


class User(models.Model):
    """
    Class to describe a user.
    """
    # TODO: hashed passwords https://docs.djangoproject.com/en/1.11/ref/contrib/auth/
    # or maybe plain text passwords that are sent in the confirmation email after login? Just do it for the meme!
    first_name = models.TextField('First Name')
    last_name = models.TextField('Last Name')
    email = models.EmailField('Email Address')


class Funeral(models.Model):
    """
    Class to describe a funeral.
    Funerals must be linked to a user
    """
    deceased = models.ForeignKey(User, 'The user whose funeral is being planned')
    date = models.DateField('Date of the funeral')
    additional_comments = models.TextField('Additional comments')
