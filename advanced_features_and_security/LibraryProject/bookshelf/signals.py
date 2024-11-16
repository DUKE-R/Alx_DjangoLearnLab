from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

def setup_groups_permissions():
    # Create Groups
    editors_group, created = Group.objects.get_or_create(name='Editors')
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    admins_group, created = Group.objects.get_or_create(name='Admins')
    
    # Assign Permissions
    book_content_type = ContentType.objects.get_for_model(Book)
    
    # Assigning Permissions to Editors
    can_create = Permission.objects.get(codename='can_create', content_type=book_content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=book_content_type)
    editors_group.permissions.set([can_create, can_edit])
    
    # Assigning Permissions to Viewers
    can_view = Permission.objects.get(codename='can_view', content_type=book_content_type)
    viewers_group.permissions.set([can_view])
    
    # Assigning Permissions to Admins
    admins_group.permissions.set([can_create, can_edit, can_view, can_delete])
    
    editors_group.save()
    viewers_group.save()
    admins_group.save()
