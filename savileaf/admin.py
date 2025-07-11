from django.contrib import admin
from .models import *

@admin.register(DropdownMenuItem)
class DropdownMenuItemAdmin(admin.ModelAdmin):
    list_display = ['label', 'url_name', 'order', 'active']
    list_editable = ['order', 'active']
    ordering = ['order']


admin.site.register(FooterService)