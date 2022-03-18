from django.db import models

class NEREntityQuerySet(models.QuerySet):
    def load_tag(self):
        return self.select_related('tag')

class NEREntityManager(models.Manager):
    
    def get_queryset(self):
        return NEREntityQuerySet(self.model, using=self._db)

    def find_by_document_id(self, document_id: int):
        return self.get_queryset().filter(document__id = document_id).load_tag()


