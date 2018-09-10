from rest_framework import serializers
from groups.models import Group, User

class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'groups', ]
        read_only_fields = ['pk']

class GroupSerializer(serializers.ModelSerializer):
    users_list = serializers.SerializerMethodField()

    def get_users_list(self, instance):
        return [i.username for i in instance.user_set.all()]

    class Meta:
        model = Group
        fields = ['pk', 'name', 'users_list', ]
        read_only_fields = ['pk']

    def validate_name(self, value):
        qs = Group.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")
        return value