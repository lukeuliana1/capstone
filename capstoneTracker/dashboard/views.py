from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.context_processors import csrf
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required(login_url='/account/login/')
def description_page(request):
    return render_to_response('dashboard/dashboard.html', {"project":True}, RequestContext(request))