from django.db import models

# Create your models here.
from django.db.models import Model


class User(Model):
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Case(Model):
    name = models.CharField(max_length=200)
    describe = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    posture = models.CharField(max_length=100)#four posture + other
    position = models.CharField(max_length=100)#inplace or move here to there
    time = models.DateTimeField()
    duration = models.IntegerField()
    def __str__(self):
        return self.name

class UnitData(Model):
    IEPC = models.CharField(max_length=200)
    Time = models.TimeField()
    Phase = models.IntegerField()
    RSSI = models.IntegerField()
    Doppler = models.IntegerField()
    Case = models.ForeignKey(Case,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

