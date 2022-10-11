from rest_framework.views import APIView
from rest_framework.response import Response

class homeApiView(APIView):
  def get(self, request, format=None):
    return Response({"nome": "Michelle Cordeiro", "idade": 26}, status=200)