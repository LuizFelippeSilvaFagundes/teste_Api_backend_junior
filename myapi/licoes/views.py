from rest_framework import viewsets
from .models import Licao
from .serializers import LicaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class LicaoViewSet(viewsets.ModelViewSet):
    queryset = Licao.objects.all()
    serializer_class = LicaoSerializer

    @action(detail=True, methods=['post'])
    def editar_html(self, request, pk=None):
        licao = self.get_object()
        conteudo_html = request.data.get('conteudo_html')
        if conteudo_html:
            licao.conteudo_html = conteudo_html
            licao.save()
            return Response({'status': 'HTML atualizado com sucesso!'})
        return Response({'error': 'Conteúdo HTML inválido'}, status=400)
