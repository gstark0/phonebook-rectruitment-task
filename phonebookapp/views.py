from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'phonebookapp/index.html')

def editPerson(request, person_id):
    return HttpResponse(person_id)

def deletePerson(request, person_id):
    return HttpResponse(person_id)