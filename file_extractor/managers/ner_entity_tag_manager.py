from django.db import models

class NEREntityTagQuerySet(models.QuerySet):
    pass

class NEREntityTagManager(models.Manager):
    
    def get_queryset(self):
        return NEREntityTagQuerySet(self.model, using=self._db)

        


