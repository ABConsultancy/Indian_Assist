from django.shortcuts import render

def index(request):
    return render(request, 'User/signin.html')
