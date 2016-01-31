from account.forms import UserCreationForm
from account.models import UserProfile as User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.db import IntegrityError
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext


def login(request):
    if request.user.is_authenticated():
        return redirect(profile)
    if 'email' in request.POST and 'password' in request.POST:
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # if request.GET["next"]:
            # return HttpResponseRedirect(request.GET["next"])
            return HttpResponse("success", content_type="text/plain")
        else:
            return HttpResponse("Either Password or Email is wrong", content_type="text/plain")
    else:
        return render_to_response('account/login.html', RequestContext(request))


def register(request):
    if request.user.is_authenticated():
        return redirect(profile)
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username = request.POST.get('email', '')
                password = request.POST.get('password', '')
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponse("success", content_type="text/plain")
            except IntegrityError as e:
                if "duplicate key value violates unique constraint \"auth_user_username_key\"" in e.message:
                    return HttpResponse("Email is already taken", content_type="text/plain")
                return HttpResponse(e.message, content_type="text/plain")
        else:
            # Check for errors
            return JsonResponse(form.errors)
    return render_to_response('account/login.html', RequestContext(request))

@login_required(login_url='/account/login/')
def profile(request):
    return render_to_response('account/profile.html', RequestContext(request))

def logout(request):
    auth.logout(request)
    return render_to_response('account/login.html', RequestContext(request))
