from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect

from home.models import Setting, ContactForm, ContactMessage, FAQ
from products.models import Category, Product, Images, Comment

from django.contrib import messages

from home.forms import SearchForm  # for search

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
    category = Category.objects.all()
    products_list = Product.objects.all().order_by('title')




    context = {
        'products': products,
        'category': category,
        'products_list' : products_list,

    }
    template_name = 'home/category_products.html'
    return render(request, template_name, context)


def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            catid = form.cleaned_data['catid']
            if catid==0:
                products=Product.objects.filter(title__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(title__icontains=query,category_id=catid)

            category = Category.objects.all()
            context = {'products': products, 'query':query,
                       'category': category }
            return render(request, 'home/search_products.html', context)

    return HttpResponseRedirect('/')



def search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    products = Product.objects.filter(title__icontains=q)
    results = []
    for pl in products:
      products_json = {}
      products_json = pl.title
      results.append(products_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)




def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all()
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')


    context = {
        'product': product,
        'category': category,
        'images': images,
        'comments': comments,

    }
    template_name = 'home/product_detail.html'
    return render(request, template_name, context)


def faq(request):
    category = Category.objects.all()
    
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")
    
    context = {
        'category': category,
        'faq': faq,
    }
    return render(request, 'home/faq.html', context)


