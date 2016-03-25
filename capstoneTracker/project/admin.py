from django.contrib import admin
from .models import Project
from account.models import Student

class StudentsInline(admin.TabularInline):
	model=Student
	fields = ('username', 'first_name', 'last_name', 'school', )
	#readonly_fields = ('username', 'first_name', 'last_name', 'school', )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		StudentsInline,
	]