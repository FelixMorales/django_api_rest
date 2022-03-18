from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.core.files.uploadedfile import InMemoryUploadedFile
from file_extractor.models import NEREntity, NEREntityTag
from file_extractor.common_serializers import NEREntityTagSerializer

import file_extractor.services.ner_entity_service


class NEREntityByDocumentView(APIView):    
    class OutputSerializer(serializers.ModelSerializer):
        tag = NEREntityTagSerializer()
        class Meta:
            model = NEREntity
            fields = ('id', 'sentence', 'tag', 'document')

    def get(self, request: Request, id):
        try:
            entities = file_extractor.services.ner_entity_service.get_entities_by_document(document_id=id)
            serializer = self.OutputSerializer(entities, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)