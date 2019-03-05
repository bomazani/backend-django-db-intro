from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User

class Profile(models.Model):
    avatar = models.CharField(max_length=45)
    body = models.TextField
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

class Categories(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    parentCategory = models.ForeignKey(
        'self',
        on_delete=models.CASCADE
    )

class Pages(models.Model):
    title = models.CharField(max_length=124)
    body = models.TextField
    is_published = models.BooleanField
    is_flagged = models.BooleanField
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE
    )


class Contributors(models.Model):
    pages = models.ManyToManyField(Pages)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Roles(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    contributor = models.ForeignKey(
        Contributors,
        on_delete=models.CASCADE
    )

class Permissions(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    roles = models.ManyToManyField(Roles)

class Tags(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=50)
    pages = models.ManyToManyField(Pages)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
