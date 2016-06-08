from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_extensions.fields import ResourceUriField
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.fields import (
    SnippetHyperlinkRelatedField, HighlightHyperlinkedIdentityField
)
from snippets.relations import SnippetHyperlinkedIdentityField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = SnippetHyperlinkRelatedField(
        many=True,
        view_name='snippet-detail',
        lookup_field='pk',
        read_only=True
    )  # This line is for reverse relationship

    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'email', 'snippets'
        )


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # serializer_url_field = SnippetHyperlinkedIdentityField
    url = SnippetHyperlinkedIdentityField(
        view_name="snippet-detail"
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True,
    )
    highlight = HighlightHyperlinkedIdentityField(
        view_name='snippet-highlight', format='html'
    )

    def save(self, **kwargs):
        print ("se creo una nueva instancia")
        super().save(**kwargs)

    def validate_title(self, value):
        if len(value) > 5:
            return value
        else:
            raise serializers.ValidationError("El nombre no coincide...")

    class Meta:
        model = Snippet
        fields = (
            'url', 'id', 'title', 'code', 'linenos', 'language',
            'style', 'highlight', 'user'
        )
