from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from project.models import Project

#@csrf_exempt
@login_required(login_url='/account/login/')
def description_page(request):
    project_entry = Project.manager.get(title="Capstone Tracker Project")
    return render_to_response('dashboard/dashboard.html', {"project":True,
                                                           "project_entry":project_entry,
                                                           "students":project_entry.student_set.all(),
                                                           "employees":project_entry.employee_set.all()},
                              RequestContext(request))
def profile(request):
    return render_to_response('dashboard/dashboard.html', {"profile":True},
                              RequestContext(request))