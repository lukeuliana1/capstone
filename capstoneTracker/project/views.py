from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import ProjectCreationForm
from .models import Project

def group_check(user):
    return user.groups.filter(name="Employee Users").exists()

@user_passes_test(group_check, login_url='/account/login/')
@login_required(login_url='/account/login/')
def create_project(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = ProjectCreationForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.employees = request.user
            object.save()
            return HttpResponse("success", content_type="text/plain")
        else:
            return JsonResponse(form.errors)
    form = ProjectCreationForm()
    args['form'] = form
    return render_to_response('project/create-project.html', RequestContext(request, args))