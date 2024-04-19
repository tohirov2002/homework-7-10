from rest_framework import serializers

from .models import Origin, Category, Word


class OriginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origin
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'
