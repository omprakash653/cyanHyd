from django.shortcuts import render
from datetime import datetime
from .models import Patients
from django.contrib import messages


# Create your views here.
def patient(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        patient = Patients(name=name, email=email, phone=phone, desc=desc)
        patient.save()
        messages.success(request, 'Your appointment has been sent')

    return render(request, 'patients.html',)

def appointments(request):
    allAppointments=Patients.objects.all()
    print(allAppointments)
    context={'appointments':allAppointments}
    return render(request,'appointment.html',context)