from rest_framework import serializers


class CadrsSerializer(serializers.ModelSerializer):
    cadr = serializers.ImageField()
