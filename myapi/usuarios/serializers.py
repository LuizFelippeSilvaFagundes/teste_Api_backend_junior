from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_de_nascimento', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(
            email=validated_data['email'],
            nome=validated_data['nome'],
            data_de_nascimento=validated_data['data_de_nascimento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
