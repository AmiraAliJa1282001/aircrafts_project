from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CustomLoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

@login_required(login_url='/accounts/login/')
def content_page(request):
    return render(request, 'pages/content_page.html')  # Adjusted path

def home(request):
    return render(request, 'pages/home.html')




class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Get the user's account type
        account_type = self.request.user.profile.account_type
        return reverse(f'{account_type.lower().replace(" ", "_")}_dashboard')
        

@login_required(login_url='/accounts/login/')
def portfolio_controller_dashboard(request):
    return render(request, 'dashboards/portfolio_controller.html')

@login_required(login_url='/accounts/login/')
def project_controller_dashboard(request):
    return render(request, 'dashboards/project_controller.html')

@login_required(login_url='/accounts/login/')
def maintenance_executer_dashboard(request):
    return render(request, 'dashboards/maintenance_executer.html')

@login_required(login_url='/accounts/login/')
def shop_administrator_dashboard(request):
    return render(request, 'dashboards/shop_administrator.html')

@login_required(login_url='/accounts/login/')
def customer_representative_dashboard(request):
    return render(request, 'dashboards/customer_representative.html')


class CustomLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            account_type = getattr(user.profile, 'account_type', None)
            return Response({
                'message': 'Login successful',
                'username': user.username,
                'account_type': account_type,
                'redirect_url': f'/dashboard/{account_type.lower().replace(" ", "_")}/'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)