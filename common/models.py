from django.db import models

# Create your models here.
class Domain(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    class Meta:
        app_label = 'common'
        db_table = 'c_domain'

class Status(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.PROTECT)
    name = models.CharField(max_length=155)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    class Meta:
        app_label = 'common'
        db_table = 'c_status'
        unique_together = (('domain', 'name'),)

class Attribute(models.Model):
    domain = models.ForeignKey('Domain', on_delete=models.PROTECT)
    name = models.CharField(max_length=155)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    class Meta:
        app_label = 'common'
        db_table = 'c_attribute'
        unique_together = (('domain', 'name'))
