from django.db import models

class PvYield(models.Model):
    # use the federal state's letter code as primary key
    state = models.CharField(primary_key=True, max_length=2, editable=False)
    spec_yield = models.IntegerField()
    state_full = models.CharField(max_length=20, editable=False)

    class Meta:
        ordering = ['state']
