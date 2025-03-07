from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

class tabdil(APIView):
    def post(self,request):
        value = request.data.get("value")
        first_unit = request.data.get("first_unit")
        second_unit = request.data.get("second_unit")
        match first_unit:
            case "ton":
                match second_unit:
                    case "kg":
                        value = value*1000
                    case "g":
                        value = value*1000000
                    case "mg":
                        value = value*1000000000
            case "kg":
                match second_unit:
                    case "g":
                        value = value*1000
                    case "mg":
                        value = value*1000000
                    case "ton":
                        value = value/1000
            case "g":
                match second_unit:
                    case "kg":
                        value = value/1000
                    case "mg":
                        value = value*1000
                    case "ton":
                        value = value/1000000
            case "mg":
                match second_unit:
                    case "kg":
                        value = value/1000000
                    case "g":
                        value = value/1000
                    case "ton":
                        value = value/1000000000
                
        return Response({
            "value":value
        })
# Create your views here.