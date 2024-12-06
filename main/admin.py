from django.contrib import admin
from django.contrib.auth.models import Group , User
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Yonalish)
admin.site.register(Fan)
admin.site.register(Ustoz)
