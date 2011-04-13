from django.db import models

class Surl(models.Model):
	lurl = models.CharField(max_length = 512)
	surl = models.CharField(max_length = 16,primary_key=True)
	fingerprint = models.CharField(max_length = 32)
	add_date = models.DateTimeField()

