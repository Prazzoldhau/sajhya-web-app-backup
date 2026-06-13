from django.shortcuts import render

# Create your views here.
def start_prescription(request):
    return render (request, 'prescription-page.html')