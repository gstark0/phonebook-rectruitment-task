from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/edit/', views.editPerson, name='edit_person'),
    path('<int:person_id>/add_phone/', views.addPhone, name='add_phone'),
    path('<int:person_id>/add_email/', views.addPhone, name='add_email'),
    path('add/', views.addPerson, name='add_person'),
    path('<int:person_id>/delete/', views.deletePerson, name='delete_person')
]