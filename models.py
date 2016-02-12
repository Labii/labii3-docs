from django.db import models
from common.backend import id2eid

class Docs(models.Model):
	titlename = models.CharField(max_length=1000, null=True)
	dtstamp = models.DateTimeField(null=True)
	
	def __unicode__(self):
		return self.titlename
	
	def eid(self):
		return id2eid(self.id)