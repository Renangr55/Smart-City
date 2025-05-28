from django.urls import path
from .views import (SensoresListCreateAPIView,
                    SensoresRetriveUpdateDestroyAPIView,
                    AmbientesListCreateAPIView,
                    AmbientesRetrieveUpdateDestroyAPIView,
                    HistoricoListCreateAPIView,
                    HistoricoRetriveUpdateDestroyAPIView,
                    ImportarDadosExcel,
                    importarDadosAmbiente,
                    importarHistorico
                    )

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    #Operações com Sensores
    path('api/sensores', SensoresListCreateAPIView.as_view(), name='sensoresLC'),
    path('api/sensores/<int:pk>', SensoresRetriveUpdateDestroyAPIView.as_view(), name='SensoresRUD'),

    #Operações com Ambientes
    path('api/ambientes', AmbientesListCreateAPIView.as_view(), name="ambientesLC"),
    path('api/ambientes/<int:pk>', AmbientesRetrieveUpdateDestroyAPIView.as_view(), name="AmbientesRUD"),

    #Operações com Histórico
    path('api/historico', HistoricoListCreateAPIView.as_view(), name="historicoLC"),
    path('api/historico/<int:pk>', HistoricoRetriveUpdateDestroyAPIView.as_view(), name='historicoRUD'),

    #Autenticação
    path('autenticacao/', TokenObtainPairView.as_view(), name="token_obtain_pair_view"),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),

    #Importação
    path("importando/Sensores",ImportarDadosExcel, name="Importar-sensores"),
    path("importando/Ambiente", importarDadosAmbiente, name="Importar-ambiente"),
    path("importando/Historico", importarHistorico, name='Importar-historico' )


]