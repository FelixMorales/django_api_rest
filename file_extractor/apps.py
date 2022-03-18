from django.apps import AppConfig

from file_extractor.types.ner_model import NERModel


class FileExtractorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file_extractor'

    def ready(self):
        NERModel()