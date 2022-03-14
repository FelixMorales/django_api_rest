from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from rest_framework.permissions import IsAuthenticated
from permissions import ReadOnly

from scrumboard.models import Card, List

import scrumboard.services.card_service

class ListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'name') 

class Cards(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Card
            fields = ('id', 'title', 'description')

    class InputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Card
            fields = ('title', 'description', 'story_points', 'business_value', 'list')

    def get(self, request: Request):
        try:
            cards = scrumboard.services.card_service.get_all_cards()
            serializer = self.OutputSerializer(cards, many=True)
            return Response(serializer.data)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @method_decorator(csrf_protect)
    def post(self, request: Request):
        try:
            serializer = self.InputSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            
            result = scrumboard.services.card_service.create_card(serializer.validated_data)
            output = self.OutputSerializer(result)
            return Response(output.data)
            
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CardsPaged(APIView):
    permission_classes = [IsAuthenticated]
    
    class OutputSerializer(serializers.ModelSerializer):
        list = ListOutputSerializer()

        class Meta:
            model = Card
            fields = ('id', 'title', 'description', 'list')

    def get(self, request: Request):

        paginator = PageNumberPagination()

        cards = scrumboard.services.card_service.get_cards_list()

        paginator.page_size = 2

        result_page = paginator.paginate_queryset(cards, request)

        serializer = self.OutputSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)