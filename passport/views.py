from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from passport.models import Barsa
from passport.serializer import BarsaSerializer


class BarsaViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    serializer_class = BarsaSerializer
    queryset = Barsa.objects.all()
