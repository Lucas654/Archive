from django.contrib.auth.models import User
from django.db import models


class Files(models.Model):
    path=models.CharField(max_length=255)
    my_file=models.FileField(upload_to='')
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, verbose_name='Пользователь',on_delete=models.CASCADE)

class Users(models.Model):
    username=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=255)

class AuthToken(models.Model):
    user_id=models.ForeignKey('Users',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)




