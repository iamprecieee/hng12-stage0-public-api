from rest_framework.serializers import Serializer, EmailField, URLField, DateTimeField


class DataSerializer(Serializer):
    email = EmailField()
    current_datetime = DateTimeField()
    github_url = URLField()
