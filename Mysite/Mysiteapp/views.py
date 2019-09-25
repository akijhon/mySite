from django.shortcuts import render
from .models import Images,Pimages,Pyobject,Jsobject,Phpobject,Rubyobject
# Create your views here.
def homefunc(request):
    object = Images.objects.get(pk=1)
    return render(request,'home.html',{'object':object})

def societyfunc(request):
    return render(request,'society.html')

def dartsfunc(request):
    return render(request,'darts.html')

def portfoliofunc(request):
    object_list1 = Pimages.objects.get(pk=1)
    object_list2 = Pimages.objects.get(pk=2)
    object_list3 = Pimages.objects.get(pk=3)
    object_list4 = Pimages.objects.get(pk=4)
    return render(request,'portfolio.html',{'object_list1':object_list1,'object_list2':object_list2,'object_list3':object_list3,'object_list4':object_list4})

def pyfunc(request):
    object_list = Pyobject.objects.all()
    return render(request,'py.html',{'object_list':object_list})

def jsfunc(request):
    object_list = Jsobject.objects.all()
    return render(request,'js.html',{'object_list':object_list})

def phpfunc(request):
    object_list = Phpobject.objects.all()
    return render(request,'php.html',{'object_list':object_list})

def rubyfunc(request):
    object_list = Rubyobject.objects.all()
    return render(request,'ruby.html',{'object_list':object_list})
