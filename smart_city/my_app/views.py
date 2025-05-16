from django.shortcuts import render
from .models import (Sensores,
                     Ambientes,
                     Historico)
from .serializer import (SensoresSerializer,
                        AmbientesSerializer,
                        HistoricoSerializer
)

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import pandas as pd

class PaginationConfig(PageNumberPagination):
    page_size = 3
    page_size_query_params = 'page_size'
    max_page_size = 10

# Create your views here.
class SensoresListCreateAPIView(ListCreateAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    pagination_class = PaginationConfig
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        sensor = self.request.query_params.get('sensor')
        if sensor:
            queryset = queryset.filter(nome__icontains=sensor)
        return queryset
    

class SensoresRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    pagination_class = PaginationConfig
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        sig = self.request.query_params.get('sig')
        if sig:
            queryset = queryset.filter(nome__icontains=sig)
        return queryset
    

class AmbientesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ambientes.objects.all()
    serializer_class = AmbientesSerializer
    pagination_class = PaginationConfig
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    pagination_class = PaginationConfig
        

class HistoricoRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
    pagination_class = PaginationConfig
    permission_classes = [IsAuthenticated]
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
    
class OperacaoExcel:
    def __init__(self, caminho_excel:str,nome_arquivo_excel,nome_planilha:str,indice_coluna:int):
        self.caminho_excel = caminho_excel
        self.nome_planilha = nome_planilha
        self.indice_coluna = indice_coluna
        self.nome_arquivo_excel = nome_arquivo_excel


    def lerExcel(self):
        excel_df = pd.read_csv(self.caminho_excel,index_col=self.indice_coluna)

    def AbrindoExcel(self,sheet_name,df,df1,df2,df3,df4,df5):
        df.to_excel(self.nome_arquivo_excel)
        df.to_excel(self.caminho_excel,sheet_name)
        with pd.ExcelWriter(self.caminho_excel) as writer:
            df1.to_excel(writer, sheet_name="Ambiente")
            df2.to_excel(writer, sheet_name="contador")
            df3.to_excel(writer,sheet_name="luminosidade")
            df4.to_excel(writer, sheet_name="temperatura")
            df5.to_excel(writer, sheet_name="umidade")

        
        



        
    