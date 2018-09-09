from django.shortcuts import render
from .models import User, Group

# Create your views here.
def index(request):
    return render(request, 'groups/index.html', {})

def UsersGroupsList(request):
    users = User.objects.all()
    groups = Group.objects.all()
    return render(request, 'groups/users_groups_list.html', {'users': users, 'groups': groups})
