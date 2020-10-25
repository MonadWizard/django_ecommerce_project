from django.shortcuts import render

# Create your views here.

def index(request):
    
    context = {}

    template_name = 'home/index.html'
    return render(request,template_name, context)

