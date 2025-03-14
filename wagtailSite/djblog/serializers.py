from rest_framework import serializers
from .models import DjBlogModel


class DjBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjBlogModel
        fields = '__all__'

