from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import traceback
import sys
import logging
from django.contrib import messages

logger = logging.getLogger(__name__)



def register_page(request):
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                # return redirect('register')
        context = {'form':form}
        return render(request,'testapp/registration.html',context)
