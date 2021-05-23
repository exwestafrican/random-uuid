from django.conf import settings

from rest_framework import serializers


class RandomGeneratorSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        created_at = instance.created_at.strftime(
            settings.REST_FRAMEWORK.get("DATETIME_FORMAT")
        )
        return {created_at: instance.id.hex}
