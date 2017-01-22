from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class sensor_state(models.Model):
    name = models.CharField(max_length=50, default='', unique=True)


class sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='sensor' )
    name = models.CharField(max_length=200, default='')
    seriennummer = models.FloatField(max_length=100, default='', unique=True)
    state = models.ForeignKey(sensor_state)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class sensormeasure(models.Model):
    sensor = models.ForeignKey(sensor, related_name="sensormeasurefeld")
    co2 = models.FloatField(max_length=20)
    temperature = models.FloatField(max_length=20)
    humidity = models.FloatField(max_length=20)
    vlufttemperature = models.FloatField(max_length=20)
    abgastemp = models.FloatField(max_length=20)

