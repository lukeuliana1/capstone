from account.models import Student, Employee
from django import forms
from django.core.exceptions import ValidationError
from .utils import generate_temp_password

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'password')

    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password"])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = user.email

        if commit:
            user.save()

        return user

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if not email:
            raise ValidationError("You must enter a valid email")
            # if you don't want this functionality, just remove it.
        return email

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('email',)

    def save(self, commit=True):
        user = super(EmployeeCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = generate_temp_password() #user.set_password()
        user.username = user.email

        if commit:
            user.save()

        return user

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        domain = email.split('@')[-1]
        if not email:
            raise ValidationError("You must enter a valid email")
            # if you don't want this functionality, just remove it.
        if domain != "gmail.com":
            raise ValidationError("Your email's domain must belong to @capitalone.com")
        return email
