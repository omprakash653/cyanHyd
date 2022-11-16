#from django.contrib import admin
from django.urls import path
from myapp import views
#from myapp.views import patient

urlpatterns = [
    path("", views.patient, name='patient'),
    path('appointment',views.appointments,name='appointment')
]