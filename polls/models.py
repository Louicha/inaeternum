from django.db import models
from django.contrib.auth.models import User


class Funeral(models.Model):
    """
    Class to describe a funeral.
    Funerals must be linked to a user
    """
    deceased = models.OneToOneField(User)
    date = models.DateField('Date of the Funeral')
    type = models.TextField('Type of Burial')
    location = models.TextField('Location')
    tombstone = models.BooleanField('Tombstone wanted?')
    layed_out = models.BooleanField('User wants to be layed out?')
    additional_comments = models.TextField('Additional Comments')


class UserProfile(models.Model):
    cheer = models.TextField('Words of Cheer')
    guest_list = models.TextField('Guest List')
    user = models.OneToOneField(User)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
