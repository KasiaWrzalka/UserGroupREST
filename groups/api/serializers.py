from rest_framework import serializers
from groups.models import Group, User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='userItem', read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'url']
        read_only_fields = ['pk']

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The username must be unique")
        return value


class UserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'first_name', 'last_name', 'group']
        read_only_fields = ['pk']

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The username must be unique")
        return value


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='groupItem', read_only=True)

    class Meta:
        model = Group
        fields = ['pk', 'name', 'url']
        read_only_fields = ['pk']

    def validate_name(self, value):
        qs = Group.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The name must be unique")
        return value


class GroupUsersSerializer(serializers.ModelSerializer):
    users_list = serializers.SerializerMethodField()

    def get_users_list(self, instance):
        return [i.username for i in instance.user_set.all()]

    class Meta:
        model = Group
        fields = ['pk', 'name', 'users_list']
        read_only_fields = ['pk']

    def validate_name(self, value):
        qs = Group.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The name must be unique")
        return value
