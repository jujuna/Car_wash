from django.shortcuts import render, HttpResponse, get_object_or_404
from django.core.paginator import Paginator
from .models import Washer,Car,Order
import datetime
from .forms import CarForm
from dateutil.relativedelta import relativedelta

def home(request):
    man=Washer.objects.all()
    
    return render(request, "washapp/home.html", {"washer":man})


def calculate(salary,percentage):
    if len(salary) == int(0):
        return 0
    pr=[]
    for n in salary:
        pr.append(list(n))
    full_salary=[sum(i) for i in zip(*pr)]
    int_salary=full_salary[0]
    washer_salary=(int_salary*percentage)/100
    return washer_salary

def detail(request, pk):
    today = datetime.datetime.today()
    lastMonth = today - relativedelta(months=1)
    lastYear=today- relativedelta(years=1)
    lastWeek=today-relativedelta(weeks=1)
    person=Washer.objects.get(pk=pk)
    per=person.washer.all()
    
    by_month=len(per.filter(order_date__range=[lastMonth, today]))
    by_year=len(per.filter(order_date__range=[lastYear, today]))
    by_week=len(per.filter(order_date__range=[lastWeek, today]))

    washer_percentage=person.percentage
    

    week_salary=per.values_list("price").filter(order_date__range=[lastWeek, today])
    week_salary=calculate(week_salary,washer_percentage)
    month_salary=per.values_list("price").filter(order_date__range=[lastMonth, today])
    month_salary=calculate(month_salary,washer_percentage)
    year_salary=per.values_list("price").filter(order_date__range=[lastYear, today])
    year_salary=calculate(year_salary,washer_percentage)
    
    
    

    context={
        "month":by_month,
        "year":by_year,
        "week":by_week,
        "week_salary":week_salary,
        "month_salary":month_salary,
        "year_salary":year_salary,
        "title":"Washer detail"
    }
    
    
    return render(request, "washapp/detail.html", context)


def car(request):
    car=Car.objects.all()
    page = request.GET.get('page', 1)
    paginator=Paginator(car,2)
    
    try:
        users=paginator.page(page)
    except PageNotAnInteger:
        users=paginator.page(1)
    except EmptyPage:
        users=paginator.page(paginator.num_pages)

    form=CarForm()
    if request.method=="POST":
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"washapp/cars.html", {"users":users, "form":form})