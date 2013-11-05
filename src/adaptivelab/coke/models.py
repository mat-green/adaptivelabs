from django.db import models

# Create your models here.

class Tweet(models.Model):
    message=models.CharField(max_length=255)
    sentiment=models.CharField(max_length=5)
    user_handle=models.CharField(max_length=255)
    occurances=models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.message