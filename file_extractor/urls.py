from django.urls import path

from file_extractor.views.file_extractor_views import FileExtractorView


urlpatterns = [
    path('upload', FileExtractorView.as_view(), name='upload_file'),
]