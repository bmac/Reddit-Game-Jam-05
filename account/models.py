from django.db import models
from django.contrib.auth.models import User
from monster.models import DamageReport

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    health = models.IntegerField(default=10)
    mana = models.IntegerField(default=10)

    attack = models.IntegerField(default=10)
    xp = models.IntegerField(default=10)
    
    dr = models.ForeignKey(DamageReport, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.user
