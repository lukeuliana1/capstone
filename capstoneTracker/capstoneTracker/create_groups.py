from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from account.models import UserProfile

employee_users = Group.objects.create(
    name='Employee Users')
employee_users.save()

student_users = Group.objects.create(
    name='Student Users')
student_users.save()

user_ct = ContentType.objects.get(app_label='account',
                                   model='UserProfile')


can_view_students = Permission.objects.create(
    name='Can View Students',
    codename='can_view_students',
    content_type=user_ct)
can_view_students.save()

can_view_employees = Permission.objects.create(
    name='Can View Employees',
    codename='can_view_employees',
    content_type=user_ct)
can_view_employees.save()

can_view_projects = Permission.objects.create(
    name='Can View Projects',
    codename='can_view_projects',
    content_type=user_ct)
can_view_projects.save()

can_view_teams = Permission.objects.create(
    name='Can View Teams',
    codename='can_view_teams',
    content_type=user_ct)
can_view_teams.save()

group = Group.objects.get(name='Employee Users')
group.permissions.add(can_view_students)
group.permissions.add(can_view_employees)
group.permissions.add(can_view_projects)
group.permissions.add(can_view_teams)

group = Group.objects.get(name='Student Users')
group.permissions.add(can_view_students)
group.permissions.add(can_view_projects)
group.permissions.add(can_view_teams)