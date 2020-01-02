from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'phonebookapp/index.html')

def addPerson(request, person_id):
    return render(request, 'phonebookapp/add.html')

def editPerson(request, person_id):
    return render(request, 'phonebookapp/edit.html')

def deletePerson(request, person_id):
    return HttpResponse(person_id)