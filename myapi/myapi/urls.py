from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),  # Inclui as rotas dos usuários
    path('api/', include('licoes.urls')),  # Inclui as rotas das lições
    
    # Endpoints de autenticação JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Gera o token JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Atualiza o token JWT
]
