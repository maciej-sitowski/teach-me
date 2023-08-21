from rest_framework import serializers

from missions.models import Mission


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ["id", "title", "description", "user"]
