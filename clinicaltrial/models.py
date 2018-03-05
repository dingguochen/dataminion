from django.db import models

# Create your models here.
class TrialMaster(models.Model):
    """
    full list of trials from all sources: mainly clinicaltrial.gov
    NOTE -- disable delete to this model
    """
    trial_id = models.CharField(primary_key=True, max_length=50)
    is_blacklisted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clinicaltrial'
        db_table = 'ct_trial_master'


class TrialStatus(models.Model):
    trial = models.ForeignKey('TrialMaster', on_delete=models.CASCADE)
    status = models.ForeignKey('common.Status', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'clinicaltrial'
        db_table = 'ct_trial_status'
