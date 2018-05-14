from django.http import HttpResponse


def ping(request):
    return HttpResponse("pong")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'inquiries': reverse('inquiry-list', request=request, format=format)
    })

from rest_framework import renderers
from rest_framework.response import Response
from .models import Inquiry
from rest_framework import generics

class InquiryHighlight(generics.GenericAPIView):
    queryset = Inquiry.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        inquiry = self.get_object()
        return Response(inquiry.highlighted)