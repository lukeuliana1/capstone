from django.contrib.auth.models import AbstractUser, User
from project.models import Project
from simple_email_confirmation import SimpleEmailConfirmationUserMixin
from django.db import models


class School(models.Model):

    """School - Information about a School."""

    name = models.CharField(max_length=255, null=True)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the name of a school."""
        return self.name


class UserProfile(SimpleEmailConfirmationUserMixin, AbstractUser):
	pass
    #someAdditionalVar = models.BooleanField(default=False)

class Student(UserProfile):

    """Student - Information about a Student."""

    SEMESTER_OPTIONS = (
        ('FA', 'Fall'),
        ('SP', 'Spring'),
        ('SU', 'Summer')
    )
    project = models.ForeignKey(Project)
    grad_semester = models.CharField(max_length=2, choices=SEMESTER_OPTIONS, null=True, blank=True)
    grad_year = models.PositiveIntegerField(null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'student'

class Employee(UserProfile):

    """Employee - Information about a Employee."""
    project = models.ForeignKey(Project)
    position = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'employee'