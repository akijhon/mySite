from django.contrib import admin
from django.urls import path,include
from .views import homefunc ,societyfunc,dartsfunc,portfoliofunc,pyfunc,jsfunc,phpfunc,rubyfunc

urlpatterns = [
    path('home/',homefunc,name='home'),
    path('society/',societyfunc,name='society'),
    path('darts/',dartsfunc,name='darts'),
    path('portfolio/',portfoliofunc,name='portfolio'),
    path('python/',pyfunc,name='py'),
    path('javascript/',jsfunc,name='js'),
    path('php/',phpfunc,name='php'),
    path('ruby/',rubyfunc,name='ruby')
]
