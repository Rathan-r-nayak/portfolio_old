from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import db
from django.urls import reverse
# Create your views here.
def default(request):
    # s=db.objects.all().values()
    # context={
    #     "s":s
    # }
    # template=loader.get_template("myPortfolio.html")
    # return HttpResponse(template.render(context,request))
    return render(request,"carier/myPortfolio.html")

def home(request):
    return render(request,"carier/myPortfolio.html")

def about(request):
    obj=db.objects.all().values()
    context={
        "ob":obj
    }
    template=loader.get_template("carier/bio.html")
    return HttpResponse(template.render(context,request))
    # return render(request,"bio.html")

def contact(request):
    return render(request,"carier/myPortfolio.html")

def form(request):
    return render(request,"carier/form.html")

def formdata(request):
    data1=request.POST['name']
    data2=request.POST['feed']
    ob1=db(name=data1,feed=data2)
    ob1.save()
    return HttpResponseRedirect(reverse("form"))

def deletedata(request,id):
    data=db.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("bio"))

