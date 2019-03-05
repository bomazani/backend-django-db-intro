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

class Role(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    contributor = models.ForeignKey(
        Contributor,
        on_delete=models.CASCADE
    )

class Contributor(models.Model):
    pages = models.ManyToManyField(Page)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Permission(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    roles = models.ManyToManyField(Role)

class Page(models.Model):
    title = models.CharField(max_length=124)
    body = models.TextField
    is_published = models.BooleanField
    is_flagged = models.BooleanField
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

class Category(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    parentCategory = models.ForeignKey(
        'self',
        on_delete=models.CASCADE
    )

class Tag(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=50)
    pages = models.ManyToManyField(Page)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class Flag(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
