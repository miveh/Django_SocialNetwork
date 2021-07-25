from django.contrib import admin

# Register your models here.
from user.models import Profile, Relationship

admin.site.register(Relationship)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
