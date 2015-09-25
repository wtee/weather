from django.db import models
from django.utils import timezone

class Organization(models.Model):

  type_of_org_choices = (
    ('School', 'School'),
    ('Business', 'Business'),
    ('Community Organization', 'Community Organization'),
    ('Other', 'Other'),
  )

  org_name = models.CharField(max_length=200, blank=False)
  address = models.CharField(max_length=200, blank=True)
  org_type = models.CharField(max_length=50,
                              choices=type_of_org_choices,
                              default='School',
                              blank=False)
  
  def __str__(self):
    return self.org_name

class Cancellation(models.Model):

  type_of_cancel_choices = (
    ('Cancellation', 'Cancellation'),
    ('Delay', 'Delay'),
    ('Early release', 'Early release'),
    ('Reschedule', 'Reschedule'),
    ('Other', 'Other'),
  )

  cancel_date = models.DateField(blank=False)
  organization = models.ForeignKey(Organization)
  type_of_cancel = models.CharField(max_length=50,
                                    choices=type_of_cancel_choices,
                                    default='Cancellation',
                                    blank=False)
  details = models.TextField(max_length=500, blank=True)

  def __str__(self):
    return str(self.cancel_date) + ' ' + str(self.organization) + ' ' + self.type_of_cancel 
           
           


