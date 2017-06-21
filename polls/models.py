from django.db import models
from django.contrib.auth.models import User


class UserProfileManager(models.Manager):

    def for_user(self, user):
        """
        Returns the user-profile for the user.
        """
        return self.get_or_create(user=user)[0]


class Funeral(models.Model):
    """
    Class to describe a funeral.
    Funerals must be linked to a user
    """
    user = models.OneToOneField(User)
    objects = UserProfileManager()
    date = models.DateField('Date of the Funeral')
    type = models.TextField('Type of Burial')
    location = models.TextField('Location')
    tombstone = models.BooleanField('Tombstone wanted?')
    laid_out = models.BooleanField('User wants to be laid out?')
    additional_comments = models.TextField('Additional Comments')


User.funeral = property(lambda u: Funeral.objects.for_user(u))


class UserProfile(models.Model):
    cheer = models.TextField('Words of Cheer')
    guest_list = models.TextField('Guest List')
    user = models.OneToOneField(User)
    objects = UserProfileManager()

User.profile = property(lambda u: UserProfile.objects.for_user(u))
