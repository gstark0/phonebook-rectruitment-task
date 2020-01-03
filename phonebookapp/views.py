from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

from .models import Person, Phone, Email

# Create your views here.
def index(request):
    people = Person.objects.all()
    phones = Phone.objects.all()
    return render(request, 'phonebookapp/index.html', {'people': people})

@require_http_methods(['POST'])
def addPerson(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')

    print(name, surname)

    return render(request, 'phonebookapp/add.html')

def addPhone(request):
    return HttpResponse('Works')

def addEmail(request):
    return HttpResponse('Works')

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def editPerson(request, person_id):
    person = get_object_or_404(Person, pk=person_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        
        person.name = name
        person.surname = surname

        person.save()

        return redirect('/phonebook')
    else:
        return render(request, 'phonebookapp/edit.html', {'name': person.name, 'surname': person.surname})

def deletePerson(request, person_id):
    return HttpResponse(person_id)