from django.shortcuts import render

from django.http import HttpResponse

context = {'test_words' : 'Nikal Laude', 'test' : 'jsfl;kja;lfjal;'} 

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'index.html', context)
