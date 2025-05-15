from django.urls import path
from .views import (SensoresListCreateAPIView,
                    SensoresRetriveUpdateDestroyAPIView,
                    AmbientesListCreateAPIView,
                    AmbientesRetrieveUpdateDestroyAPIView)

urlpatterns = [
    #Operações com Sensores
    path('api/sensores', SensoresListCreateAPIView.as_view(), name='SensoresLC'),
    path('api/sensores/<int:pk>', SensoresRetriveUpdateDestroyAPIView.as_view(), name='SensoresRUD')
]