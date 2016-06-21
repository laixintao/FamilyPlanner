from django.shortcuts import render

# Create your views here.

def familycalender_index(request):
    return render(request,'familycalender_index.html')