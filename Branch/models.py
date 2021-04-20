from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branches(models.Model):

    branch= models.CharField(max_length=7)

class Stu_Data(models.Model):

    #User=models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    Branches = models.OneToOneField(Branches, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=19, null=True)
    mobile = models.CharField(max_length=16, null=True)
    email = models.EmailField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=7)
    country=models.CharField(max_length=15)
    marks_percentage=models.FloatField()


    gender_choices=(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
    )


    country_choices=(

        ('AUSTRALIA','AUSTRALIA'),
        ('BANGLADESH','BANGLADESH'),
        ('CHINA','CHINA'),
        ('DENMARK','DENMARK'),
        ('EGYPT','EGYPT'),
        ('INDIA', 'INDIA'),
        ('SWEDEN','SWEDEN'),
        ('USA','USA'),
    )



    def __str__(self):
        return self.name+str(self.id)