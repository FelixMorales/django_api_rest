from django.db import models

class CardQuerySet(models.QuerySet):
   def load_list(self):
       return self.select_related('list')

class CardManager(models.Manager):
    
    def get_queryset(self):
        return CardQuerySet(self.model, using=self._db)

    def find_by_id_with_related(self, id):
        return self.get_queryset().load_list().get(pk=id)
    
    def get_list_with_related(self):
        return self.get_queryset().load_list().all().order_by('id')
        

        


