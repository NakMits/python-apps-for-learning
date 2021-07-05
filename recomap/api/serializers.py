from rest_framework import serializers
from api.models import Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    auther = serializers.CharField(max_length=100)
    tag = serializers.CharField(null=True, max_length=30)
    lat = serializers.CharField(max_length=30)
    lng = serializers.CharField(max_length=30)
    images = serializers.ImageField(upload_to='', null=True)
    memo = serializers.TextField(null=True)
    
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.auther = validated_data.get('auther', instance.auther)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lng = validated_data.get('style', instance.lng)
        instance.images = validated_data.get('style', instance.images)
        instance.memo = validated_data.get('style', instance.memo)
        instance.save()
        return instance