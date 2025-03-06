from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class tabdil(APIView):
    def post(self,request):
        value = request.data.get("value")
        unit = request.data.get("unit")
        value = value/1000
        return Response({
            "value":value
        })
        
        
# Create your views here.
