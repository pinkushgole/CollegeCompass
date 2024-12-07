from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required

CustomUser = get_user_model()

class home(APIView):
      def get(self, request):
        return render(request, "index.html")
      


class user_sign_up(APIView):
      def get(self, request):
        return render(request, "user_signup.html")
      
      def post(self, request):
        """Signup for normal users and admins."""
       
        data = request.POST
       
        print(data)

        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")
        phone = data.get("phone")
        address = data.get("address")
        is_admin = False

        # Validate input
        if not all([email, first_name, last_name, password]):
            return JsonResponse({"error": "Missing required fields."}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email is already registered."}, status=400)

       
        is_normal_user =True

        # Create user
        user = CustomUser.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            password=make_password(password),  
            is_normal_user=is_normal_user,
            is_admin=is_admin,
            is_staff=is_admin,  
        )

        return render(request, "user_login.html")


class admin_sign_up(APIView):
      def get(self, request):
        return render(request, "admin_signup.html")
      
      def post(self, request):
        """Signup for normal users and admins."""
       
        data = request.POST
       
        print(data)

        email = data.get("email")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        password = data.get("password")
        phone = data.get("phone")
        address = data.get("address")
        is_admin = True
        is_staff=True
        # Validate input
        if not all([email, first_name, last_name, password]):
            return JsonResponse({"error": "Missing required fields."}, status=400)

        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email is already registered."}, status=400)

       
        is_normal_user =False

        # Create user
        user = CustomUser.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            password=make_password(password),  
            is_normal_user=is_normal_user,
            is_admin=is_admin,
            is_staff=is_staff,  
        )

        return render(request, "admin_login.html")



class loginuser(APIView):
      def get(self, request):
        return render(request, "login.html")
      
      def post(self, request):
        """Handle user login and return appropriate response."""
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Log in the user
        login(request, user)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Render based on user type
        if user.is_admin:
            return render(request, 'home.html', {"user": user, "tokens": tokens})
        else:
            return render(request, 'index.html', {"user": user, "tokens": tokens})


@login_required
def user_logout(request):
    logout(request)
    return redirect('Home')