from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

from .models import Person, Phone, Email

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'phonebookapp/index.html', {'people': people})

@csrf_exempt
@require_http_methods(['GET', 'POST'])
def addPerson(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        new_person = Person(name=name, surname=surname)
        new_person.save()

        return redirect('/phonebook')
    else:
        return render(request, 'phonebookapp/add.html')

@require_http_methods(['GET', 'POST'])
def addPhone(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        phone_num = request.POST.get('phone')
        phone = Phone(person=person, phone=phone_num)
        phone.save()
    else:
        return render(request, 'phonebookapp/add_phone.html')

@require_http_methods(['GET', 'POST'])
def addEmail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        email_addr = request.POST.get('email')
        email = Email(person=person, email=email_addr)
        email.save()
    else:
        return render(request, 'phonebookapp/add_email.html')

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