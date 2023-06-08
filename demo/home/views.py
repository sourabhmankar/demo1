from django.shortcuts import render
from .models import student
# Create your views here.
def home(request):
    s=student.objects.all()
    return render(request,'home.html',{'student':s})