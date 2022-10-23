from django.shortcuts import render


# Create your views here.
def thingsPage(request):
    return render(request, 'thingsHome.html')
