from . import views
from django.urls import path
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Users and Groups API')

urlpatterns = [
    path('', views.api_root),
    path('schema/', schema_view),
    path('group/', views.GroupList.as_view(), name='groupList'),
    path('group/<int:pk>/', views.GroupItem.as_view(), name='groupItem'),
    path('group/<int:pk>/users/', views.GroupItemWithUsers.as_view(), name='groupItemWithUsers'),
    path('user/', views.UserList.as_view(), name='userList'),
    path('user/<int:pk>/', views.UserItem.as_view(), name='userItem'),
    path('user/<int:pk>/groups/', views.UserItemWithGroups.as_view(), name='userItemWithGroups'),
]
