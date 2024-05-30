from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Quotes
from .serializers import QuoteSerializer

class MotivationalQuoteRetrieveView(generics.RetrieveAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
