from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from .models import *

def test_view(request):
    return HttpResponse("Salom Dunyo")

def home_view(request):
    return render(request, "home.html")

def fan_view(request):
    fan = Fan.objects.all()
    context = {"fanlar": fan}
    return render(request, "fan.html", context)

def fan_delete_view(request,fan_id):
    fan = get_object_or_404(Fan, id=fan_id)
    fan.delete()
    return redirect("fanlar")

def yonalish_view(request):
    yonalish = Yonalish.objects.all()
    context = {"yonalishlar": yonalish}
    return render(request, "yonalish.html", context)

def yonalish_delete_view(request,yonalish_id):
    yonalish = get_object_or_404(Yonalish, id=yonalish_id)
    yonalish.delete()
    return redirect("yonalish")

def ustoz_view(request):
    ustoz = Ustoz.objects.all()
    qsoz1 = request.GET.get("qsoz1")

    if qsoz1 is not None:
        ustoz = Ustoz.objects.filter(ism__icontains=qsoz1)

    context = {"ustozlar": ustoz, 'qsoz1': qsoz1}
    return render(request, "ustoz.html", context)

def ustoz_delete_view(request,ustoz_id):
    ustoz = get_object_or_404(Ustoz, id=ustoz_id)
    ustoz.delete()
    return redirect("ustoz")