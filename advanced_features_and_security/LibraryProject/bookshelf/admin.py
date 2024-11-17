from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

    from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app.models import Article

# Create groups
editors_group, _ = Group.objects.get_or_create(name='Editors')
viewers_group, _ = Group.objects.get_or_create(name='Viewers')
admins_group, _ = Group.objects.get_or_create(name='Admins')

# Get permissions
content_type = ContentType.objects.get_for_model(Article)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

# Assign permissions
editors_group.permissions.add(can_create, can_edit)
viewers_group.permissions.add(can_view)
admins_group.permissions.add(can_create, can_view, can_edit, can_delete)

from django.contrib.auth.models import User
user = User.objects.get(username='editor_user')
user.groups.add(editors_group)
