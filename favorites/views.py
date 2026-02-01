from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Favorite
from .serializers import FavoriteSerializer


# ⭐ Add favorite
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_favorite(request):
    serializer = FavoriteSerializer(data=request.data, context={"request": request})

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 📄 List favorites
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    serializer = FavoriteSerializer(favorites, many=True)
    return Response(serializer.data)


# 🗑️ Delete favorite
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_favorite(request, pk):
    try:
        favorite = Favorite.objects.get(pk=pk, user=request.user)
        favorite.delete()
        return Response(
            {"message": "Favorite deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

    except Favorite.DoesNotExist:
        return Response(
            {"error": "Favorite not found"},
            status=status.HTTP_404_NOT_FOUND
        )
