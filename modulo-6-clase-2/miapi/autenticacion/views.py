from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class MensajeSecretoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensaje": "Contenido Secreto!"})


class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"mensaje": "Contenido Secreto para Admin!"})
