from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Language
from .serializers import LanguageSerializer

@api_view(['GET'])
def language_list(request):
    languages = Language.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)
