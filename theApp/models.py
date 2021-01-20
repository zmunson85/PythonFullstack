from django.db import models
import re

# Create your models here.


class UserManager(models.Manager):
    def validator(self, postdata):
        errors = {}

        if len(postdata['first_name']) < 2:
            errors["first_name"] = "Entry must be more than two characters"
        if len(postdata['last_name']) < 2:
            errors["last_name"] = "Entery must be more than 2 characters"
        if len(postdata['password']) < 8:
            errors["password"] = "Please enter at least 8 characters"
        if postdata['password'] != postdata['confirm_pass']:
            errors["confirm_pass"] = "Your entries must match"
        if len(postdata['password']) < 8:
            errors["login_password"] = "Inccorect Password"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid email address!"
        emailExist = User.objects.filter(email=postdata['email'])
        if emailExist:
            errors['email_exist'] = "That email exists"
        return errors

    def login_validator(self, postdata):
        errors = {}
        # validating email
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postdata['email_login']):
            errors['email_login'] = "Not a valid email!"
            # if email exist
        emailExist = User.objects.filter(email=postdata['email_login'])
        if not emailExist:
            errors['email_notfound'] = "This email does not exist"

            return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=255)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    message = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    message_wall = models.ForeignKey(Message, related_name="post_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
