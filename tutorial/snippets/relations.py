from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.reverse import reverse


class SnippetHyperlinkedIdentityField(HyperlinkedIdentityField):

    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            'parent_lookup_user': obj.user_id,
            'pk': obj.pk
        }
        #import ipdb; ipdb.set_trace()
        url = reverse(
            view_name, kwargs=url_kwargs, request=request, format=format
        )
        return url
