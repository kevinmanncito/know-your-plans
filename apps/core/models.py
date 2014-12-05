from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    employer = models.ForeignKey('Employer')
    member_number = models.BigIntegerField(blank=True, null=True)


class Employer(models.Model):
    name = models.CharField(max_length=255)
    open_enroll_start = models.DateField()
    open_enroll_end = models.DateField()
    enroll_url = models.CharField(max_length=255)