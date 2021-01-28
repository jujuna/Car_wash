from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import HireCompany, Location, WasherCompany

# Create your views here.
def most_common(l):
    return max(set(l), key=l.count)

def home(request):
    comp=WasherCompany.objects.all()
    loc=Location.objects.all()
    li=[i.city for i in loc]
    common_city=most_common(li)
    
    return render(request, "washapp/home.html", {"company":comp, "location":loc, "common":common_city})

def company_order(request, pk):
    order=HireCompany.objects.get(company=pk)
    return render(request, "washapp/detail.html", {"order":order})
    