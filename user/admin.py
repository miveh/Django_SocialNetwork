from django.contrib import admin

# Register your models here.
from user.models import User, Relationship

admin.site.register(Relationship)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
