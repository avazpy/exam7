from django.shortcuts import render, redirect
from apps.models import Person


def person(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'index.html', context)


def delete_person(request, pk):
    Person.objects.filter(id=pk).delete()
    return redirect('persons')
