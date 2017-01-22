from django.contrib import admin
from accounts.models import UserProfile, sensor_state, sensor, sensormeasure

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(sensor_state)
admin.site.register(sensor)
admin.site.register(sensormeasure)