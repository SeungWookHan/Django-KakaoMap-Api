from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MapInfo
from django.shortcuts import render

# Create your views here.


class ViewMap(APIView):
    def get(self, request):
        return render(request, "kakaomap/kakaomap.html")
