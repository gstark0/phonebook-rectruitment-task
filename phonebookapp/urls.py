from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/edit/', views.editPerson, name='edit'),
    path('<int:person_id>/add/', views.addPerson, name='add'),
    path('<int:person_id>/delete/', views.deletePerson, name='edit')
]