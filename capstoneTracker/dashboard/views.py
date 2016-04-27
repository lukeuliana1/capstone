from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from project.models import Project
from account.models import School

#@csrf_exempt


@login_required(login_url='/account/login/')
def project_page_user(request):
    if request.user.is_student() and request.user.student.project is not None:
        project_entry = request.user.student.project
        return render_to_response('dashboard/project.html', {"project_entry": project_entry, "students": project_entry.student_set.all(), "sponsors": project_entry.sponsors.all(), "project_menu":True}, RequestContext(request))
    elif request.user.is_employee():
        return redirect(profile_page) #Case when Employee has multiple projects, idk which project to show, thus redirecting to profile
    else:
        raise Http404

def project_page_request(request):
    project_slug = request.path.split('/')[-1]
    project_entry = Project.manager.filter(slug=project_slug)[0]
    if project_entry is not None:
        return render_to_response('dashboard/project.html', {"project_entry": project_entry, "students": project_entry.student_set.all(), "sponsors": project_entry.sponsors.all(), "project_menu":True}, RequestContext(request))
    else:
        raise Http404


@login_required(login_url='/account/login/')
def profile_page(request):
    project_set = []
    if request.user.is_student():
        project_set.append(request.user.student.project)
        return render_to_response('dashboard/profile.html', {'project_set':project_set, 'profile_menu':True}, RequestContext(request))
    elif request.user.is_employee():
        project_set = request.user.employee.project_set.all()
        return render_to_response('dashboard/profile.html', {'project_set':project_set, 'profile_menu':True}, RequestContext(request))
    else:
        raise Http404

@login_required(login_url='/account/login/')
def global_page(request):
    projects = Project.manager.all()
    schools = School.objects.all()
    return render_to_response('dashboard/global.html', {'projects':projects, 'schools':schools, 'global_menu':True} , RequestContext(request))
