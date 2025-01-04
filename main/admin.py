from django.contrib import admin
from django.contrib.auth.models import Group , User
from .models import *

class UstozAdmin(admin.ModelAdmin):
    list_display = ('ism' , 'jins' , 'fan')

    search_fields = ['ism',]
    search_help_text = "Ism orqali qidiring"

class YonalishAdmin(admin.ModelAdmin):
    list_display = ('nom',)

    list_filter = ('nom',)
    search_fields = ['nom',]
    search_help_text = "Nom orqali qidiring"

class FanAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('yonalish',)
    search_fields = ['nom',]
    search_help_text = "Nom orqali qidiring"

admin.site.register(Yonalish , YonalishAdmin)
admin.site.register(Fan, FanAdmin)
admin.site.register(Ustoz , UstozAdmin)

admin.site.unregister(Group)
admin.site.unregister(User)
