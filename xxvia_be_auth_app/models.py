from django.db import models

#Authentication Model created

class User(models.Model):
    username = models.CharField(max_length=30, blank=False, default='')
    password = models.CharField(max_length=300,blank=False, default='')
    firstname = models.CharField(max_length=60, blank=False, default='')
    lastname = models.CharField(max_length=60, blank=False, default='')
    emailaddress = models.EmailField(max_length=240, blank=False, default='')
    userrole = models.CharField(max_length=20, blank=False, default='Customer')
    creationdate = models.DateTimeField(auto_now_add=True)
    updatedate = models.DateTimeField(auto_now=True)