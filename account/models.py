from django.db import models
from django.shortcuts import render
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.utils import timezone
# Create your models here.


class profile(models.Model):
	alphanumeric_email = RegexValidator(r'^[0-9a-zA-Z@.]*$', 'Only Email characters are allowed.')
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z@.]*$', 'Only alphanumeric characters are allowed.')
	username = models.CharField(max_length=30,blank=False,null=False,unique=True)
	first_name = models.CharField(max_length=30,blank=False,null=False)
	last_name = models.CharField(max_length=30,blank=False,null=False)
	aadharid = models.IntegerField()
	email = models.CharField(max_length=20,null=True,validators=[alphanumeric_email])
	hospital = models.CharField(max_length=70,null=True,blank=True)
	experience = models.IntegerField(blank=True,null=True)
	designation = models.CharField(max_length=50,blank=True)
	nationality = models.CharField(max_length=20,null=True)

	def __str__(self):
		return self.first_name+' '+self.last_name

	def name(self):
		return self.first_name+' '+self.last_name

class qualifications(models.Model):
	doctor = models.ForeignKey(profile,on_delete=models.CASCADE)
	qualification = models.CharField(max_length=60,blank=False,null=False)

	def __str__(self):
		return self.qualification

class children(models.Model):
	alphanumeric_email = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only Email characters are allowed.')
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z@.]*$', 'Only alphanumeric characters are allowed.')
	parent = models.ForeignKey(profile,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30,blank=False,null=False)
	last_name = models.CharField(max_length=30,blank=False,null=False)
	age = models.IntegerField()

	def __str__(self):
		return self.first_name+' '+self.last_name

class operations(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
	pur = models.CharField(max_length=200,blank=False,null=False,validators=[alphanumeric])
	bhamasahof = models.CharField(max_length=50,null=True, validators=[alphanumeric])
	username = models.CharField(max_length=30,null=True)
	aadharhof = models.CharField(max_length=50, blank=False, null=False, validators=[alphanumeric])
	hospital = models.CharField(max_length=50,null=True,validators=[MinLengthValidator(10)])
	date = models.DateField(default=timezone.now())