from rest_framework import serializers


class ArchiveSerializer(serializers.Serializer):
    path=serializers.CharField(max_length=255)
    my_file=serializers.FileField()
    name=serializers.CharField(max_length=255)
    created_at=serializers.DateTimeField()
    user_id_id = serializers.IntegerField()

class UserSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()