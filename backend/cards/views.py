from rest_framework.exceptions import status
from cards.models import Card
from rest_framework.response import Response
from rest_framework.views import APIView

from cards.serializers.common import CardSerializer


# Create your views here.


class CardList(APIView):
    def get(self, _request, format=None):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
