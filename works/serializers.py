from rest_framework import serializers
from .models import CreativeWork

class CreativeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreativeWork
        fields = ['id', 'title', 'page_link', 'source', 'retrieved_at']
