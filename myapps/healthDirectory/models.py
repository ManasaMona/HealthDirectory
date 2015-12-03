from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class Service_provider(models.Model):
	ser_name = models.CharField(max_length=50)
	ser_spl = models.CharField(max_length=200)
	ser_email =models.EmailField()
	ser_psword=models.CharField(max_length=200)
	ser_phNum=models.BigIntegerField()
	ser_addr=models.CharField(max_length=75)
	ser_location=models.CharField(max_length=50)

	# def __unicode__(self):
	# return self.ser_name
	def __unicode__(self):
		return smart_unicode(self.ser_name)


