from django.contrib.auth.models import AbstractUser, User
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin
from django.db import models
from os import path

def image_upload_path(instance, filename):
    return path.join("school-avatars/"+"-".join((instance.name, str(instance.id)))+"/", filename)


class School(models.Model):

    """School - Information about a School."""

    name = models.CharField(max_length=255, null=True)
    school_avatar = models.ImageField(upload_to=image_upload_path, blank=True)
    contact_first_name = models.CharField(max_length=255)
    contact_last_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=35, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return the name of a school."""
        return self.name


class UserProfile(SimpleEmailConfirmationUserMixin, AbstractUser):

    def is_employee(self, *args, **kwargs):
        if hasattr(self, 'employee'):
            return True
        else:
            return False

    def is_student(self, *args, **kwargs):
        if hasattr(self, 'student'):
            return True
        else:
            return False

class Student(UserProfile):

    """Student - Information about a Student."""

    SEMESTER_OPTIONS = (
        ('FA', 'Fall'),
        ('SP', 'Spring'),
        ('SU', 'Summer')
    )
    project = models.ForeignKey('project.Project', blank=True, null=True, on_delete=models.CASCADE)
    grad_semester = models.CharField(max_length=2, choices=SEMESTER_OPTIONS, null=True, blank=True)
    grad_year = models.PositiveIntegerField(null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    school = models.ForeignKey(School, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'student'
        permissions = (
            ("can_view_students", "Can View Students"),
            ("can_view_projects", "Can View Projects"),
            ("can_view_teams", "Can View Teams"),
        )

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Student, self).save(*args, **kwargs)

class Employee(UserProfile):

    """Employee - Information about a Employee."""
    position = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'employee'
        permissions = (
            ("can_view_students", "Can View Students"),
            ("can_view_projects", "Can View Projects"),
            ("can_view_teams", "Can View Teams"),
            ("can_view_employees", "Can View Employees")
        )

    def save(self, *args, **kwargs):
        self.username = self.email
        super(Employee, self).save(*args, **kwargs)