from django.contrib import admin
from .models import Images,Pimages,Pyobject,Jsobject,Phpobject,Rubyobject
# Register your models here.
admin.site.register(Images)
admin.site.register(Pimages)
admin.site.register(Pyobject)
admin.site.register(Jsobject)
admin.site.register(Phpobject)
admin.site.register(Rubyobject)
