
# Old 
# --- 
# from django.shortcuts import render

# # Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Old
# ---
# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('age_details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))