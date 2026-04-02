from django.shortcuts import render

# Create your views here.
def myprodject_view(request):
    return render(request, 'myprodject/myprodject.html')