from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Department(models.Model):
      name = models.CharField(max_length=100,null=False)
      location = models.CharField(max_length=100)

      def __str__(self):
         return self.name


class Employee(models.Model):
     first_name = models.CharField(max_length=5, null=False, blank=False )
     last_name = models.CharField(max_length=100, null=False , blank=False)
     salary = models.IntegerField(0)
     # position = models.CharField(max_length=20, null=False, blank=False)
     dept = models.ForeignKey(Department , on_delete = models.CASCADE)


     def __str__(self):
          return "%s %s "%(self.first_name, self.last_name)


# class Task(models.Model):
#      employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
#      status = models.
