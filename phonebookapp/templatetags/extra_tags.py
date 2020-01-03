from django import template
register = template.Library()

@register.filter
def by_person(objects, person):
    return objects.filter(person=person)