from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from products.models import Category 
from user.models import UserProfile

from user.forms import SignUpForm


@login_required(login_url='/login') # Check login
def index(request):
    category = Category.objects.all()
    current_user = request.user  # Access User Session information
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {'category': category,
               'profile':profile}
    return render(request,'user/user_profile.html',context)



def login_form(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user =request.user
            userprofile=UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url

            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Login Error !! Username or Password is incorrect")
            return HttpResponseRedirect('/user/login')
    # Return an 'invalid login' error message.

    category = Category.objects.all()
    context = {'category': category
     }

    template_name = 'user/login_form.html'
    return render(request, template_name, context)





def signup_form(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/user/signup')


    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }

    template_name = 'user/signup_form.html'
    return render(request, template_name, context)


def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')





