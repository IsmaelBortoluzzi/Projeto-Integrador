from django.contrib import admin
from .models import *


class AddressAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
