from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from project.models import Project
from account.models import School

#@csrf_exempt


@login_required(login_url='/account/login/')
def project_page_user(request):
    if hasattr(request.user, 'student') and request.user.student.project is not None:
        project_entry = request.user.student.project
        return render_to_response('dashboard/project.html', {"project_entry": project_entry, "students": project_entry.student_set.all(), "employees": project_entry.employee_set.all(), "project_menu":True}, RequestContext(request))
    else:
        raise Http404

def project_page_request(request):
    return None


@login_required(login_url='/account/login/')
def profile_page(request):
    return render_to_response('dashboard/profile.html', {'profile_menu':True}, RequestContext(request))


@login_required(login_url='/account/login/')
def global_page(request):
    projects = Project.manager.all()
    schools = School.objects.all()
    return render_to_response('dashboard/global.html', {'projects':projects, 'schools':schools, 'global_menu':True} , RequestContext(request))
