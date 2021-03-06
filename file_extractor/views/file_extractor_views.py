from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from django.core.files.uploadedfile import InMemoryUploadedFile
from file_extractor.models import NEREntity, NEREntityTag

import file_extractor.services.file_extractor_service
from file_extractor.common_serializers import NEREntityTagSerializer

class FileExtractorView(APIView):    
    parser_classes = [FileUploadParser]

    class OutputSerializer(serializers.ModelSerializer):
        tag = NEREntityTagSerializer()
        class Meta:
            model = NEREntity
            fields = ('id', 'sentence', 'tag', 'document')

    def put(self, request):
        try:
            file_obj: InMemoryUploadedFile = request.data['file']
            entities = file_extractor.services.file_extractor_service.parse_file(file=file_obj)

            serializer = self.OutputSerializer(entities, many=True)
            return Response(serializer.data)
            
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)