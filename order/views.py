from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from order.models import ShopCart, ShopCartForm
from products.models import Category, Product
# Create your views here.



def index(request):
    return HttpResponse ("Order Page")


# def addtoshopcart(request,id):
#     return HttpResponse(str(id))
@login_required(login_url='/login') # Check login
def addtoshopcart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user  # Access User Session information

    checkproduct = ShopCart.objects.filter(product_id=id)  # Check product in shopcart
    if checkproduct:
        control = 1 # The product is in the cart
    else:
        control = 0 # The product is not in the cart"""


    if request.method == 'POST':  # if there is a post
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control==1: # Update  shopcart
                data = ShopCart.objects.get(product_id=id)
            
                data.quantity += form.cleaned_data['quantity']
                data.save()  # save data
            else : # Inser to Shopcart
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id =id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Product added to Shopcart ")
        return HttpResponseRedirect(url)

    else: # if there is no post
        if control == 1:  # Update  shopcart
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()  #
        else:  #  Inser to Shopcart
            data = ShopCart()  # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()  #
        messages.success(request, "Product added to Shopcart")
        return HttpResponseRedirect(url)




def shopcart(request):

    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for pl in shopcart:
        total += pl.product.price * pl.quantity
    #return HttpResponse(str(total))
    context={'shopcart': shopcart,
             'category':category,
             'total': total,
             }

    template_name = 'order/shopcart_products.html'
    
    return render(request,template_name, context) 

@login_required(login_url='/login') # Check login
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item deleted form Shopcart.")
    return HttpResponseRedirect("/order/shopcart")






