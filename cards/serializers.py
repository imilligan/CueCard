from cards.models import Card, Source, Author
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
	citation = serializers.PrimaryKeyRelatedField(many=False, read_only=False)

	class Meta:
		model = Card
		fields = ('info', 'code', 'citation', 'start_page', 'end_page')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Author
		fields = ('first', 'middle', 'last')

class SourceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Source
		fields = ('title', 'author')
