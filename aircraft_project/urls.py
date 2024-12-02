from users import views
from django.contrib import admin
from django.urls import path, include
from users.admin import admin_site 
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),  # Add this line
    
]
