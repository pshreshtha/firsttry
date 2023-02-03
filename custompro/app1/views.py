from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InventSerializers
from .models import Inventory

class Add_Invent_API(APIView):
    serializer = InventSerializers

    def get(self, request):
        pro = Inventory.objects.all()
        serializer = self.serializer(pro, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
