from account.models import Student, Employee
from django import forms
from django.core.exceptions import ValidationError
from .utils import generate_temp_password
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model

from django.utils.http import urlsafe_base64_encode

from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template import loader
from django.conf import settings

class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'password')

    def save(self, commit=True):
        user = super(StudentCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(generate_temp_password())
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
        user.set_password(generate_temp_password())
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
        if domain != settings.ALLOWED_EMAIL_DOMAIN:
            raise ValidationError("Your email's domain must belong to @capitalone.com")
        return email

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.

        """
        active_users = get_user_model()._default_manager.filter(
            email__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        email = self.cleaned_data["email"]
        users = self.get_users(email)
        if len(list(users)) == 0:
            raise ValidationError("No such user exists")
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }

            self.send_mail(subject_template_name, email_template_name,
                           context, from_email, user.email,
                           html_email_template_name=html_email_template_name)

