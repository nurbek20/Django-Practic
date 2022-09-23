from django.contrib import admin
from covidapp.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id', 'last_name', 'first_name', 'email', 'number')


admin.site.register(Contact, ContactAdmin)