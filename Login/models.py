from django.contrib.auth.models import User
from django.db import models
from PIL import Image



class profile(models.Model):
    user = models.ForeignKey(User)
   
    full_name = models.CharField(max_length=100,blank=True)
    photo_upload=models.FileField(blank=True)
    date_of_birth=models.DateField(blank=True,default='2001-01-01')
    pincode=models.IntegerField(blank=True,default=0)
    present_address=models.CharField(blank=True,max_length=200)
    gender=models.CharField(blank=True,max_length=6)
    permanent_address=models.CharField(max_length=200,blank=True)

    father_name=models.CharField(max_length=100,blank=True)
    father_employment=models.CharField(max_length=100,blank=True)
    father_phone=models.IntegerField(default=0)

    mother_name = models.CharField(max_length=100,blank=True)
    mother_employment = models.CharField(max_length=100,blank=True)
    mother_phone = models.IntegerField(default=0)

    bank_name=models.CharField(max_length=100,blank=True)
    bank_type=models.CharField(max_length=100,blank=True)
    pan_number=models.CharField(max_length=16,default=0)
    bank_branch=models.CharField(max_length=100,blank=True)

    checkforcerti=models.CharField(max_length=5,blank=True)
    checkforexperience=models.CharField(max_length=5,blank=True)
    checkforaddress=models.CharField(max_length=5,blank=True)


class Qualification(models.Model):
    user=models.ForeignKey(User)
    course=models.CharField(max_length=100,blank=True,default=None)
    university=models.CharField(max_length=100,blank=True,default=None)
    fromyear=models.PositiveSmallIntegerField(default=0,blank=True)
    toyear=models.PositiveSmallIntegerField(default=0,blank=True)
    grade=models.PositiveSmallIntegerField(default=0,blank=True)


class Experience(models.Model):
    user=models.ForeignKey(User)
    profile=models.CharField(max_length=100,blank=True)
    company=models.CharField(max_length=100,blank=True)
    fromyear=models.PositiveSmallIntegerField(default=0)
    toyear=models.PositiveSmallIntegerField(default=0)
    ctc=models.PositiveSmallIntegerField(default=0)
    designation=models.CharField(max_length=100,blank=True)
	
class Certificate(models.Model):
	user=models.ForeignKey(User)
	course=models.CharField(max_length=100,blank=True)
	institute=models.CharField(max_length=100,blank=True)
	fromyear=models.PositiveSmallIntegerField(default=0)
	toyear=models.PositiveSmallIntegerField(default=0)
	descp=models.CharField(max_length=100,blank=True)