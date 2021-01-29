from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Washer,Car,Order
import datetime
from dateutil.relativedelta import relativedelta

def home(request):
    man=Washer.objects.all()
    # a=man.washer.all()
    # b=a.filter(order_date__year="2021")
    # print(len(b))
    return render(request, "washapp/home.html", {"washer":man})
    

def detail(request, pk):
    today = datetime.datetime.today()
    lastMonth = today - relativedelta(months=1)
    lastYear=today- relativedelta(years=1)
    lastWeek=today-relativedelta(weeks=1)
    person=Washer.objects.get(pk=pk)
    a=person.washer.all()
    by_month=len(a.filter(order_date__range=[lastMonth, today]))
    by_year=len(a.filter(order_date__range=[lastYear, today]))
    by_week=len(a.filter(order_date__range=[lastWeek, today]))

    washer_percentage=person.percentage
    mon=[]
    for i in a:
        mon.append(i.price)
        
    sum_money=sum(mon)
    money=(washer_percentage*sum_money)/100
    
    return render(request, "washapp/detail.html", {"person":person, "month":by_month, "year":by_year, "week":by_week,"money":money})
