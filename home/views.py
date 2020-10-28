from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Setting, ContactForm, ContactMessage
from django.contrib import messages
# Create your views here.

def index(request):

    setting = Setting.objects.get(pk=1)





    # contact us form.......start.........

    if request.method == 'POST': # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage() #create relation with model
            data.name = form.cleaned_data['name'] # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  #save data to table
            messages.success(request,"Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('')

    setting = Setting.objects.get(pk=1)
    form = ContactForm



    # contact us form.......end.........


    context = {'setting': setting, 'form':form}

    template_name = 'home/index.html'
    return render(request,template_name, context)















