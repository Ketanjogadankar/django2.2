from django.contrib import  admin

from django.contrib import  admin
from sign_up.models import Post
from django.contrib.auth.admin import UserAdmin


class postAdmin(admin.ModelAdmin):
    list_display = ['post','author']



admin.site.register(Post)

