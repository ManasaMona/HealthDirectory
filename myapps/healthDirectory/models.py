from django.db import models

# Create your models here.
class Service_Provider(models.Model):
   ser_name = models.CharField(max_length=50)
   ser_spl = models.CharField(max_length=200)
   ser_email =models.CharField(max_length=200)
   ser_psword=models.CharField(max_length=200)
   ser_phNum=models.CharField(max_length=15)
   ser_addr=models.CharField(max_length=75)
   ser_location=models.CharField(max_length=50)
   
   def __unicode__(self):
        return self.ser_name
   

