from django.shortcuts import render

def home(request):
    return render (request, 'home.html')

def about(request):
    return render (request, 'about.html')

def resume(request):
    return render (request, 'resume.html')

def contacts(request):
    return render (request, 'contacts.html')

def cert(request):
    return render (request, 'cert.html')