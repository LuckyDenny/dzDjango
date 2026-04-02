from django.shortcuts import render

# Create your views here.
def clients_view(request):
    return render(request, 'clients/clients.html')