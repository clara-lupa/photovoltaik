from django.db import models

class PvYield(models.Model):
    # use the federal state's letter code as primary key
    state = models.CharField(primary_key=True, max_length=2, editable=False)
    spec_yield = models.IntegerField()

    class Meta:
        ordering = ['state']
