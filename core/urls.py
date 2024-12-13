from main.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', home_view),
    path('fanlar/', fan_view, name='fanlar'),
    path('ustozlar/', ustoz_view, name='ustozlar'),
    path('yonalishlar/', yonalish_view, name='yonalishlar'),
    path('fanlar/<int:fan_id>/delete/', fan_delete_view),
    path('yonalishlar/<int:yonalish_id>/delete/', yonalish_delete_view),
    path('ustozlar/<int:ustoz_id>/delete/', ustoz_delete_view),
]
