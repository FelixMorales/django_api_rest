from django.db import models

class DocumentQuerySet(models.QuerySet):
    pass

class DocumentManager(models.Manager):
    
    def get_queryset(self):
        return DocumentQuerySet(self.model, using=self._db)

        


