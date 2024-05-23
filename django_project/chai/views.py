from django.shortcuts import render

from .models import ChaiVariety


# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, "chai/all_chai.html", {"chais": chais})
