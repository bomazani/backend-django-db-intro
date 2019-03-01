from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User

class Users(models.Model):
    id = INT
    username = models.VARCHAR(45)
    password = models.VARCHAR(45)
    email = VARCHAR(45)

class Profiles(models.Model):
    id = Int
    user_id = INT
    avatar = VARCHAR(45)
    body = TEXT

class Roles(models.Model):
    id = INT
    title = VARCHAR(45)

class Contributors(models.Model):
    page_id = INT
    user_id = INT
    role_id = INT

class Permissions(models.Model):
    id = INT
    title = VARCHAR(45)

class Pages(models.Model):
    id=INT
    user_id = INT
    category_id = INT
    title = VARCHAR(124)
    body = LONGTEXT
    is_published = TINYINT
    is_flagged = TINYINT

class Categories(models.Model):
    id = INT
    user_id = INT
    parent_id = INT
    title = VARCHAR(30)

class Tags(models.Model):
    id = INT
    user_id = INT
    body = VARCHAR(50)
