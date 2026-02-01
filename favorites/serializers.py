from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = "__all__"
        read_only_fields = ["user"]

    def create(self, validated_data):
        favorite, created = Favorite.objects.get_or_create(
            user=self.context["request"].user,
            **validated_data
        )
        return favorite
