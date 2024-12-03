from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('api/login/', views.CustomLoginAPIView.as_view(), name='api_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('content/', views.content_page, name='content_page'), 
    path('portfolio-controller/', views.portfolio_controller_dashboard, name='portfolio_controller_dashboard'),
    path('project-controller/', views.project_controller_dashboard, name='project_controller_dashboard'),
    path('maintenance-executer/', views.maintenance_executer_dashboard, name='maintenance_executer_dashboard'),
    path('shop-administrator/', views.shop_administrator_dashboard, name='shop_administrator_dashboard'),
    path('customer-representative/', views.customer_representative_dashboard, name='customer_representative_dashboard'),
   

]
