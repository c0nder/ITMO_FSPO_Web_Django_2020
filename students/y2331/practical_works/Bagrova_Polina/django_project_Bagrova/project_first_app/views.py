from django.http import Http404
from django.shortcuts import render
from project_first_app.models import Owner


def details(request, owner_id):
    try:
        o = Owner.objects.get(pk=owner_id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': o})
