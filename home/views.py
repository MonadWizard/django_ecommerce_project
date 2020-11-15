from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactForm, ContactMessage
from products.models import Category, Product

from django.contrib import messages
# Create your views here.

def index(request):

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    products_slider = Product.objects.all().order_by('-id')[:4]  # first 4 product
    products_latest = Product.objects.all().order_by('id')[:4]  # last 4 product
    products_picked = Product.objects.all().order_by('?')[:4]  # Random selected 4 product



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


    context = {
                'setting': setting, 'form':form, 
                'category': category, 
                'products_slider': products_slider,
                'products_latest': products_latest,
                'products_picked': products_picked,

                }

    template_name = 'home/index.html'
    return render(request,template_name, context)


def category_products(request, id, slug):
    products = Product.objects.filter(category_id=id)
    return HttpResponse(products)














