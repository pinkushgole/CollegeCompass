
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('home/',home.as_view(),name="Home" ),

    path('login-user/',loginuser.as_view(),name="login_user" ),
    path('logout/', user_logout, name='user_logout'),

    path('user-sign-up/',user_sign_up.as_view(),name="user_sign_up" ),
   


    path('admin-sign-up/',admin_sign_up.as_view(),name="admin_sign_up" ),
   
]
