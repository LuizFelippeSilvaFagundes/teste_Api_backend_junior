from rest_framework import viewsets, permissions
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
