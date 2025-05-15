from django.shortcuts import render
from .models import (Sensores,
                     Ambientes,
                     Historico)
from .serializer import (SensoresSerializer,
                        AmbientesSerializer,
                        HistoricoSerializer
)
from rest_framework.authentication import authenticate
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import BasePagination
from rest_framework.response import Response
from rest_framework import status

class PaginationConfig(BasePagination):
    page_size = 3
    page_size_query_params = 'page_size'
    max_page_size = 10

# Create your views here.
class SensoresListCreateAPIView(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    pagination_class = PaginationConfig

class SensoresRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    pagination_class = PaginationConfig
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(SensoresSerializer,data=request.data,partial=partial) 
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 

        if getattr(instance,'_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Mensagem' : 'Sensor Deletado'}, status=status.HTTP_204_NO_CONTENT)

class AmbientesListCreateAPIView(ListCreateAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    pagination_class = PaginationConfig

class AmbientesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    pagination_class = PaginationConfig
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'Mensagem' : 'A Classe: Ambiente foi listado'},serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(Ambientes,data=request.data,partial=partial) 
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 

        if getattr(instance,'_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Mensagem' : 'Ambiente deletado'}, status=status.HTTP_204_NO_CONTENT)


class HistoricoListCreateAPIView(ListCreateAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    pagination_class = PaginationConfig

class HistoricoRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    pagination_class = PaginationConfig
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'Mensagem' : 'A Classe: Histórico foi listado' },serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(SensoresSerializer,data=request.data,partial=partial) 
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer) 

        if getattr(instance,'_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Mensagem" : "Histórico deletado com sucesso"})