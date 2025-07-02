from django.db import models


class Student(models.Model):    # this line represents Django model named Student, models.Model indicates Django model
    name = models.CharField(max_length=225)
    gender = models.CharField(max_length=25)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.gender} - {self.dob} - {self.email} - {self.phone}"
