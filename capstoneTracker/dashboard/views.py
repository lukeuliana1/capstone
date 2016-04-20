from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from project.models import Project

#@csrf_exempt
@login_required(login_url='/account/login/')
def project_page(request):
    project_entry = Project.manager.get(title="Capstone Tracker Project")
    return render_to_response('dashboard/project.html', {"project_entry":project_entry,
                                                           "students":project_entry.student_set.all(),
                                                           "employees":project_entry.employee_set.all()},
                              RequestContext(request))
@login_required(login_url='/account/login/')
def profile_page(request):
    return render_to_response('dashboard/profile.html', RequestContext(request))

@login_required(login_url='/account/login/')
def global_page(request):
    return render_to_response('dashboard/global.html', RequestContext(request))