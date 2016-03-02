from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm)
from .forms import PasswordResetForm

from django.contrib.auth.tokens import default_token_generator
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import login as system_auth
from account.forms import EmployeeCreationForm
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from account.utils import send_confirmation_email
from django.views.decorators.debug import sensitive_post_parameters
from django.shortcuts import resolve_url
from django.views.decorators.cache import never_cache
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.conf import settings

@csrf_protect
@sensitive_post_parameters()
@never_cache
def login(request):
    if request.user.is_authenticated():
        return redirect(profile)
    if request.method == 'POST' and 'email' in request.POST and 'password' in request.POST:
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_confirmed:
            auth.login(request, user)
            # if request.GET["next"]:
            # return HttpResponseRedirect(request.GET["next"])
            return HttpResponse("success", content_type="text/plain")
        else:
            return HttpResponse("Credentials are not valid", content_type="text/plain")
    else:
        return render_to_response('account/auth.html', {"auth":True}, RequestContext(request))

@csrf_protect
@sensitive_post_parameters()
@never_cache
def register_employee(request):
    args = {}
    if request.user.is_authenticated():
        return redirect(profile)
    if request.method == 'POST' and 'email' in request.POST:
        args['form'] = EmployeeCreationForm()
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                user.groups.add(Group.objects.get(name='Employee Users'))
                send_confirmation_email(user)
                return HttpResponse("success", content_type="text/plain")
            except IntegrityError as e: #Duplicate email error
                if 1062 in e.args:
                    return HttpResponse("Email is already taken", content_type="text/plain")
                return HttpResponse(e.message, content_type="text/plain")
        else: #Form errors
            # Check for errors
            return JsonResponse(form.errors)
    return render_to_response('account/auth.html', {"auth":True}, RequestContext(request))

def confirm_email(request):
    args = {}
    if request.method == "GET" and 'key' in request.GET and 'user' in request.GET:
        try:
            user = get_user_model().objects.get(username=request.GET["user"])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if not user.is_confirmed:
                user.confirm_email(request.GET["key"])
                system_auth(request, user)
                return redirect(password_change)
            else:
                raise Http404("Wrong data, reject request")
        except:
            raise Http404("Wrong data, reject request")
    else:
        raise Http404("Wrong data, reject request")

        

@login_required(login_url='/account/login/')
def profile(request):
    return render_to_response('account/profile.html', RequestContext(request))

@never_cache
def logout(request):
    auth.logout(request)
    return redirect(login)

"""
    Overriden functions from django.auth
"""

@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='account/auth.html',
                    password_change_form=SetPasswordForm,
                    extra_context=None):
    if request.method == "POST":
        form = password_change_form(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Updating the password logs out all other sessions for the user
            # except the current one.
            update_session_auth_hash(request, form.user)
            return redirect(profile)
    else:
        form = password_change_form(request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)

    return render_to_response(template_name, context, RequestContext(request))


@csrf_protect
def forgot_password(request,
                   from_email=settings.DEFAULT_FROM_EMAIL,
                   html_email_template_name='email/forgot-password.html',
                   email_template_name='email/forgot-password.txt',
                   subject_template_name='email/password_reset_subject.txt',
                   token_generator=default_token_generator):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            try:
                opts = {
                    'use_https': request.is_secure(),
                    'token_generator': token_generator,
                    'from_email': from_email,
                    'email_template_name': email_template_name,
                    'subject_template_name': subject_template_name,
                    'request': request,
                    'html_email_template_name': html_email_template_name,
                }
                form.save(**opts)
                return HttpResponse("success")
            except ValidationError as e:
                return HttpResponse(e.message, content_type="text/plain")
    else:
        form = PasswordResetForm()
    return render_to_response('account/auth.html', {"form" : form }, RequestContext(request))

# Override for django.contrib.auth.views.password_reset_confirm
# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='account/auth.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                system_auth(request, user)
                return redirect(profile)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        return HttpResponse("Password reset unsuccessful, please start process again")
    context = {
        'form': form,
        'validlink': validlink,
    }
    if extra_context is None:
        extra_context = {"auth" : False}
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return render_to_response(template_name, context, RequestContext(request))
