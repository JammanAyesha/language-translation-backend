import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def translate_text(request):
    """
    Django API view to translate text using LibreTranslate.
    Expects JSON:
    {
        "text": "Good morning",
        "source": "en",
        "target": "hi"
    }
    """

    # Validate input
    text = request.data.get("text")
    source = request.data.get("source")
    target = request.data.get("target")

    if not text or not source or not target:
        return Response(
            {"error": "Missing 'text', 'source', or 'target' in request."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Forward request to LibreTranslate
        libre_response = requests.post(
            "http://127.0.0.1:5000/translate",
            json={
                "q": text,
                "source": source,
                "target": target,
                "format": "text"
            },
            timeout=30
        )
        libre_response.raise_for_status()  # Raises HTTPError for bad responses

        # Return LibreTranslate response directly
        return Response(libre_response.json())

    except requests.exceptions.RequestException as e:
        return Response(
            {"error": "Translation service unavailable", "details": str(e)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )
