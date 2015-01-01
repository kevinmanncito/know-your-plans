from django.db import models


class Member(models.Model):
    member_number = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    organization = models.ForeignKey('Organization')

    def __unicode__(self):
        return "{0} {1} - {2}".format(self.firstname, self.lastname, self.member_number)


class SalesChannel(models.Model):
    sales_channel_number = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.name)


class Organization(models.Model):
    organization_number = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    open_enroll_start = models.DateField()
    open_enroll_end = models.DateField()
    sales_channel = models.ForeignKey(SalesChannel)
    enroll_url = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.name)


class Carrier(models.Model):
    short_name = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.name)


class Plan(models.Model):
    plan_number = models.CharField(unique=True, max_length=255)
    logo = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    carrier = models.ForeignKey(Carrier, related_name='plans')
    plan_type = models.ForeignKey('PlanType')
    organization = models.ForeignKey(Organization, related_name='plans')
    copays = models.CharField(max_length=255, default="100.00")
    individual_deductable = models.DecimalField(decimal_places=2, 
                                                max_digits=12,
                                                default=1.00)
    family_deductable = models.DecimalField(decimal_places=2, 
                                            max_digits=12,
                                            default=1.00)
    co_insurance = models.DecimalField(decimal_places=2, 
                                       max_digits=3,
                                       default=1.00)
    moop_individual = models.DecimalField(decimal_places=2, 
                                          max_digits=12,
                                          default=1.00)
    moop_family = models.DecimalField(decimal_places=2, 
                                      max_digits=12,
                                      default=1.00)
    meta_info = models.ManyToManyField('PlanMetaInfo',
                                       blank=True,
                                       null=True)

    def __unicode__(self):
        return "{0}".format(self.name)


class Level(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2, max_digits=12)
    plan = models.ForeignKey(Plan)

    def __unicode__(self):
        return "{0}".format(self.name)


class PlanType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.name)


class PlanMetaInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return "{0}".format(self.name)





