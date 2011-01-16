from django.db import models

# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length=255)
    health = models.IntegerField(default=10)
    xp = models.IntegerField(default=10)
    description = models.TextField(blank=True)
    pic = models.ImageField(upload_to="monster_img")

    def __unicode__(self):
        return "%s" % self.name


class DamageReport(models.Model):
    monster = models.ForeignKey(Monster)
    damage = models.IntegerField(default=0)
