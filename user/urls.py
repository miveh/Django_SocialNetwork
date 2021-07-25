from django.urls import path
from .views import *
urlpatterns = [
    path('profile_view/', profile_view, name='profile_view'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('profile_id/<int:id>', profile_view_by_id, name='profile_view_by_id')
]