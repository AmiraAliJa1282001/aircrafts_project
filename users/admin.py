from django.contrib import admin


# Create a custom AdminSite class
class CustomAdminSite(admin.AdminSite):
    site_header = 'Aircraft Maintenance Engineering Admin'  # The title in the admin panel header
    site_title = 'Aircraft Maintenance Engineering'         # The title in the browser tab
    index_title = 'Welcome to the Aircraft Maintenance Admin' # The title in the admin index page

# Instantiate the custom admin site
admin_site = CustomAdminSite(name='custom_admin')

# Register your models with the custom admin site
# Example: admin_site.register(ModelName)
# admin_site.register(ModelName)  # Register your models here

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
