from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import traceback
import sys
import logging
from django.contrib import messages
from .forms import CreateUserForms   #Created mannually

logger = logging.getLogger(__name__)



def register_page(request):
        # form = UserCreationForm() #Importing base django usercreationform
        form = CreateUserForms()
        if request.method == 'POST':
            # form = UserCreationForm(request.POST)    #Importing base django usercreationform
            form = CreateUserForms(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                # return redirect('register')
        context = {'form':form}
        return render(request,'testapp/registration.html',context)


def login_page(request):
    context = { }
    return render(request, 'testapp/login.html', context)



