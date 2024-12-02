from rest_framework import serializers


class JanrsSerializer(serializers.ModelSerializer):
    janr = serializers.CharField(max_length=250)
