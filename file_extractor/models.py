from django.db import models

from file_extractor.managers.document_managers import DocumentManager
from file_extractor.managers.ner_entity_manager import NEREntityManager
from file_extractor.managers.ner_entity_tag_manager import NEREntityTagManager

class Document(models.Model):
    aws_file_link = models.CharField(max_length=500)
    
    objects = models.Manager()
    manager = DocumentManager()

    def __str__(self):
        return f'Document: {self.aws_file_link} ({self.id})'

class NEREntityTag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    
    objects = models.Manager()
    manager = NEREntityTagManager()

    def __str__(self):
        return f'Tag: {self.name} ({self.id})'

class NEREntity(models.Model):
    sentence = models.TextField()
    tag = models.ForeignKey(NEREntityTag, on_delete=models.CASCADE, related_name='sentences')
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='sentences')

    objects = models.Manager()
    manager = NEREntityManager()

    def __str__(self):
        return f'NER Sentence: {self.sentence} ({self.id})'