from rest_framework import mixins, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from passport.models import Barsa, Profile
from passport.serializer import BarsaSerializer, ProfileSerializer


class BarsaViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   GenericViewSet):
    serializer_class = BarsaSerializer
    queryset = Barsa.objects.all()


class ProfileViewSet(mixins.CreateModelMixin,
                     GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        profile = get_object_or_404(self.queryset, login=request.data.get('login'))
        if profile.password == request.data.get('password'):
            return Response({'user_id': profile.id}, status=status.HTTP_200_OK)

        return Response({'error': 'Incorrect password'}, status=status.HTTP_401_UNAUTHORIZED)
