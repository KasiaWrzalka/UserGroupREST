
from rest_framework import generics, mixins
from .serializers import GroupSerializer
from groups.models import Group

class GroupAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = GroupSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Group.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Group.objects.all()
