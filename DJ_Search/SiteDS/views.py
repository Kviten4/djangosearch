from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request, "mysearch/index.html")
def imagesearch(request):
     return render(request, "mysearch/imagesearch.html")
def advancedsearch(request):
     return render(request, "mysearch/advancedsearch.html")