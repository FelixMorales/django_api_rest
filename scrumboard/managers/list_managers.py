from django.db import models

class ListQuerySet(models.QuerySet):
    def load_cards(self):
        return self.prefetch_related('cards')

class Listanager(models.Manager):
    
    def get_queryset(self):
        return ListQuerySet(self.model, using=self._db)

    def find_by_id_with_related(self, id):
        return self.get_queryset().load_cards().get(pk=id)
        
    def get_list_with_related(self):
        return self.get_queryset().load_cards().all().order_by('id')


