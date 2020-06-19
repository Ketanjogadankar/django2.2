from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import traceback
import sys
import logging
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CreateUserForms, HomeForm   #Created mannually
from .models import Post
from django.urls import reverse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist


logger = logging.getLogger(__name__)


def register_page(request):
    if request.user.is_authenticated:   #User could not type user "localhost:/login/" & go to login page once he is logged in already
        return redirect('home')
    else:
        # form = UserCreationForm() #Importing base django usercreationform
        form = CreateUserForms()
        if request.method == 'POST':
            # form = UserCreationForm(request.POST)    #Importing base django usercreationform
            form = CreateUserForms(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created successfully for' + user)
                return redirect('sign_up:login')
        context = {'form':form}
        return render(request,'testapp/registration.html',context)

def login_page(request):
    if request.user.is_authenticated:    #User could not type user "localhost:/login/" & go to login page once he is logged in already
        return redirect('sign_up:blog')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            logger.error("Could not read %s", user)


            if user is not None:
                login(request, user)
                return redirect('sign_up:blog')
            else:
                messages.info(request, 'Username or Password is incorrect')


        context = { }
        return render(request, 'testapp/login.html', context)


# @login_required(login_url='login')
# def home_page(request):
#     # logger.error("request>>>>>>>>>>>>>", request)
#
#     return  render(request, 'testapp/home.html')

def logout_user(request):
    logout(request)
    return redirect('sign_up:login')

def get(request):
    form = HomeForm()
    return render(request, {'form':form})


# def article_detail()

class Post_blog(View):
    # try:
    #     coach_instance = Post.objects.get(author=request.user)
    # except Post.DoesNotExist:
    #     coach_instance = Post(author=request.user)
    # t=0
    def get(self, request, *args, **kwargs):
        form = HomeForm()
        try:
            posts_obj = Post.objects.filter(author=request.user)
            context = {
                'post': posts_obj,
                'form': form
                }
            return render(request, 'testapp/home.html', context)
        except ObjectDoesNotExist:
            return render(request, 'testapp/home.html')

    def post(self, request, *args, **kwargs):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            post.author = request.user
            logger.error("anonymous................>>>>>>")
            text = form.cleaned_data["post"]
            # Post.objects.get_or_create(post=text)
            user_cnf = Post.objects.create(author=request.user, post=text)
            user_cnf.save()                  #It can be use to save data send by user in DB
            # form.save()                   #It can be use to save data send by user in DB

            # form = HomeForm()
            return redirect('sign_up:blog')
            # post_ref = Post(post=text, author=request.user)
            # post_ref.save()
        else:
            pass

        # args = {'form':form,'text':text}
        return  redirect('sign_up:blog')






