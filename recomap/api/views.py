from rest_framework import viewsets
from recomap.models import MarkerModel
from api.serializers import SnippetSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = MarkerModel.objects.all()
    serializer_class = SnippetSerializer