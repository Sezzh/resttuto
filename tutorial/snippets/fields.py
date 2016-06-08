from rest_framework.relations import (
    HyperlinkedRelatedField, HyperlinkedIdentityField
)
from rest_framework.reverse import reverse
from snippets.models import Snippet


class SnippetHyperlinkRelatedField(HyperlinkedRelatedField):
    """
    This custom field works for nested resources.
    """

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'parent_lookup_user': obj.user_id,
            'pk': obj.pk,
        }
        url = reverse(
            view_name, kwargs=url_kwargs, request=request, format=format
        )
        return url


class HighlightHyperlinkedIdentityField(HyperlinkedIdentityField):

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'parent_lookup_user': obj.user_id,
            'pk': obj.pk,
        }
        url = reverse(
            view_name, kwargs=url_kwargs, request=request, format=format
        )
        return url
