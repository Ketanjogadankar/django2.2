from django.urls import path
from .  import views

app_name = 'sign_up'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('blog/', views.Post_blog.as_view(), name='blog'),
    path('register/', views.register_page, name='register'),
     # path('home/', views.home_page, name='home'),
]