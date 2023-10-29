from django.contrib import admin
from home.models import Contact
# Register your models here.

class Name(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(Contact,Name)

