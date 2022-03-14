from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from scrumboard.models import List, Card

import scrumboard.services.list_service

class CardOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title') 

class Lists(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = List
            fields = ('id', 'name')

    def get(self, request: Request):
        try:
            lists = scrumboard.services.list_service.get_all_lists()
            serializer = self.OutputSerializer(lists, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ListsPaged(APIView):

    class OutputSerializer(serializers.ModelSerializer):
        cards = CardOutputSerializer(many=True)

        class Meta:
            model = List
            fields = ('id', 'name', 'cards')

    def get(self, request: Request):

        paginator = PageNumberPagination()

        lists = scrumboard.services.list_service.get_lists()

        paginator.page_size = 2

        result_page = paginator.paginate_queryset(lists, request)

        serializer = self.OutputSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)