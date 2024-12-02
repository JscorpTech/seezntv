from rest_framework import serializers


class VideoFileSerializer(serializers.ModelSerializer):
    url = serializers.CharField(max_length=700)
    index = serializers.IntegerField()
    quality = serializers.CharField(max_length=250)
