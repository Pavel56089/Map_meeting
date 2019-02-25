from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    group = models.IntegerField()
    lyceum = models.CharField(max_length=20)
    about = models.TextField()
    transport = models.TextField()
    vk = models.URLField(default = 'vk.com')
    kxInt = models.BigIntegerField(default = '55')
    kxDecimal = models.BigIntegerField(default = '684758')
    kyInt = models.BigIntegerField(default = '37')
    kyDecimal = models.BigIntegerField(default = '738521')
