from django.db import models
from django.contrib.auth.models import  User
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser



# Create your models here.
# username:mayur200
# emailid:mayur.pardeshi96@gmail.com
# pass:aai123

# Create your models here.

class User(AbstractUser):
    pass

class Post(models.Model):

    REQUIRED_FIELDS = ('user',)


    post = models.CharField(max_length=500)
    USERNAME_FIELD = 'post'

    # upostser = models.ForeignKey(User, on_delete=models.CASCADE,  default='none')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,)


    def post_save_receiver(sender, instance, created, **kwargs):
        pass

    post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)



