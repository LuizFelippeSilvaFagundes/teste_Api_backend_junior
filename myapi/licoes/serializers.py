from rest_framework import serializers
from .models import Licao

class LicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licao
        fields = ['id', 'titulo', 'conteudo_html']
