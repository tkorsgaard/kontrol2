from django.db import models

# Create your models here.

class DateTryout(models.Model):
    name = models.CharField(max_length=250)
    when = models.DateTimeField('Event date')


class Person(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    has_work = models.BooleanField()
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return "<Person: %s = Work: %s>" % (self.full_name, self.has_work)
