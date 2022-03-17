from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from django.core.files.uploadedfile import InMemoryUploadedFile

import file_extractor.services.file_extractor_service


class FileExtractorView(APIView):    
    parser_classes = [FileUploadParser]

    class OutputSerializer(serializers.Serializer):
        text = serializers.CharField()

    def put(self, request):
        try:
            file_obj: InMemoryUploadedFile = request.data['file']
            text = file_extractor.services.file_extractor_service.get_file_text(file=file_obj)

            output = self.OutputSerializer(data={'text' : text})
            output.is_valid(raise_exception=True)
            
            return Response(output.data)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)