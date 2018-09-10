from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name

    def users_of_group(self):
        return list(self.user_set.all())

class User(models.Model):
    username = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.username
