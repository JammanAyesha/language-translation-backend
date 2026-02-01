from rest_framework import serializers

class TranslationSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=10)
    target = serializers.CharField(max_length=10)
    text = serializers.CharField()