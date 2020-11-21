from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from products.models import CommentForm, Comment
# Create your views here.

def indexP(request):
   return  HttpResponse("My Product Page")


# def addcomment(request):
#    return HttpResponse("Add Comment")

def addcomment(request,id):
   url = request.META.get('HTTP_REFERER')  # get last url
   # return HttpResponse(url)        # for test
   if request.method == 'POST':  # check post
      form = CommentForm(request.POST)
      if form.is_valid():
         data = Comment()  # create relation with model
         data.subject = form.cleaned_data['subject']
         data.comment = form.cleaned_data['comment']
         data.rate = form.cleaned_data['rate']  
         data.ip = request.META.get('REMOTE_ADDR')
         data.product_id=id
         current_user= request.user
         data.user_id=current_user.id
         data.save()  # save data to table
         messages.success(request, "Your review has ben sent. Thank you for your interest.")
         return HttpResponseRedirect(url)

   return HttpResponseRedirect(url)












