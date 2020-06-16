from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Candidates!! Welcome to the DJANGO TRAINING")

def index2(request):
    return render(request,"boot_app/home.html")