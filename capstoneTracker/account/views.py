from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.context_processors import csrf
from django.db import IntegrityError
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import login as system_auth
from account.forms import StudentCreationForm, EmployeeCreationForm
from django.contrib.auth import get_user_model
from account.utils import send_confirmation_email

def auth_check(user):
    return (not user.is_authenticated())

@user_passes_test(auth_check, login_url='/account/profile/')
def login(request):
    if request.method == 'POST' and 'email' in request.POST and 'password' in request.POST:
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # if request.GET["next"]:
            # return HttpResponseRedirect(request.GET["next"])
            return HttpResponse("success", content_type="text/plain")
        else:
            return HttpResponse("Credentials are not valid", content_type="text/plain")
    else:
        return render_to_response('account/login.html', RequestContext(request))


@user_passes_test(auth_check, login_url='/account/profile/')
def register_employee(request):
    args = {}
    args.update(csrf(request))
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
                if "duplicate key value violates unique constraint \"auth_user_username_key\"" in e.message:
                    return HttpResponse("Email is already taken", content_type="text/plain")
                return HttpResponse(e.message, content_type="text/plain")
        else: #Form errors
            # Check for errors
            return JsonResponse(form.errors)
    return render_to_response('account/login.html', RequestContext(request))

def confirm_email(request):
    args = {}
    if request.method == "GET" and 'key' in request.GET and 'user' in request.GET:
        try:
            user = get_user_model().objects.get(username=request.GET["user"])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.confirm_email(request.GET["key"])
            system_auth(request, user)
            return redirect(profile)
        except:
            raise Http404("Wrong data, reject request")

        

@login_required(login_url='/account/login/')
def profile(request):
    return render_to_response('account/profile.html', RequestContext(request))

def logout(request):
    auth.logout(request)
    return render_to_response('account/login.html', RequestContext(request))
