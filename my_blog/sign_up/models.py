from django.db import models
from django.contrib.auth.models import  User
from django.conf import settings


# Create your models here.
# username:mayur200
# emailid:mayur.pardeshi96@gmail.com
# pass:aai123

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default='don')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)



