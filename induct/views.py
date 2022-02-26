from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import inducts,induct_2
from django.contrib.auth.mixins import LoginRequiredMixin

class list_view(ListView):
    model = inducts,induct_2
    fields = '__all__'
    context_object_name = "induct-list"

def showdata(request):
    disp = inducts.objects.all()
    disp2 = induct_2.objects.all()
    return render(request,"induct/inducts_list.html",{"display": disp,"display1": disp2}
    )

def home(request):
    return render(request,"users/layout.html",{
    })





