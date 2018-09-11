from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import GroupSerializer, UserSerializer, GroupUsersSerializer, UserGroupsSerializer
from groups.models import Group, User

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'group': reverse('groupList', request=request, format=format),
        'user': reverse('userList', request=request, format=format)
    })


class GroupList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = GroupSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Group.objects.all()


class GroupItemWithUsers(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupUsersSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Group.objects.all()


class UserList(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = UserSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserItem(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()


class UserItemWithGroups(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserGroupsSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return User.objects.all()

