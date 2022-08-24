from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def hesAccess(request):
    return render(request, 'hesaccess.html')

def meterDetails(request):
    return render(request, 'meterDetails.html')
