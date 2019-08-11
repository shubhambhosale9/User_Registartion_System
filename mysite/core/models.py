from django.db import models
from django import forms
#from django.contrib.auth.models import AbstractUser, AuthUserManager
from django.contrib.auth.models import Group, UserManager as AuthUserManager, \
    AbstractUser, update_last_login

class UserManager(AuthUserManager):
    """
    UserManager to create superuser.
    """
    use_in_migrations = True

    def get_queryset(self):
        """
        Overwritten predefined function to filter the queryset on the basis of soft delete status.
        :return:
        """
        return super(UserManager, self).get_queryset().filter()


    def get_deleted_users(self):
        """
        This function filters queryset on the basis of soft delete status and returns list of
        deleted users
        :return:
        """
        return super(UserManager, self).get_queryset().filter()


class User(AbstractUser):
    CHOICES= [('YES', 'YES'), ('NO', 'NO'),]
    #username = models.CharField(max_length=30)
    #role = models.ForeignKey(Role, help_text='Users Role')
    web_address = models.CharField(max_length=30)
    cover_letter = models.CharField(max_length = 500)
    file = models.FileField()
    work_choice = models.CharField(choices=CHOICES, max_length=32)
    #objects = UserManager()
