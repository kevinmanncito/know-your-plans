from rest_framework import viewsets

from .serializers import MemberSerializer
from apps.core import models


# ViewSets define the view behavior.
class MemberViewSet(viewsets.ModelViewSet):
    queryset = models.Member.objects.all()
    serializer_class = MemberSerializer