from django.urls import path

from file_extractor.views.file_extractor_views import FileExtractorView
from file_extractor.views.ner_entity_views import NEREntityByDocumentView


urlpatterns = [
    path('upload', FileExtractorView.as_view(), name='upload_file'),
    path('entities/document/<int:id>', NEREntityByDocumentView.as_view(), name='document_entities'),
]