from rest_framework import serializers
from file_extractor.models import NEREntityTag

class NEREntityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = NEREntityTag
        fields = ('id', 'name', 'description')