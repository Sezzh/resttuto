from rest_framework.serializers import HyperlinkedRelatedField
from rest_framework.reverse import reverse
from snippets.models import Snippet


class SnippetHyperlinkRelatedField(HyperlinkedRelatedField):
    view_name = 'snippet-detail'
    queryset = Snippet.objects.all()

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'parent_lookup_user': obj.user_id,
            'pk': obj.pk
        }
        reverse(view_name, kwargs=url_kwargs, request=request, format=format)
