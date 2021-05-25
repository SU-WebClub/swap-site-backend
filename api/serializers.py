from rest_framework.serializers import ModelSerializer, CharField, StringRelatedField, MultipleChoiceField
from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Blog, Category, Role, Tag, Author, News

class AuthorSenderSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class TagSenderSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySenderSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(ModelSerializer):
    category = CharField(source='category.name')
    tags = StringRelatedField(many=True, read_only=True)
    author = AuthorSenderSerializer()

    class Meta:
        model = Blog
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    role = RoleSerializer

    class Meta:
        model = Author
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    author = AuthorSenderSerializer()
    tags = TagSenderSerializer()
    category = CategorySenderSerializer()

    class Meta:
        model = Blog
        fields = '__all__'
        
class NewsSerializer(serializers.ModelSerializer):
    author = AuthorSenderSerializer()

    class Meta:
        model = News
        fields = '__all__'
