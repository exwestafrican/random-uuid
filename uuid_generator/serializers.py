from rest_framework import serializers


class RandomGeneratorSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {instance.created_at: instance.id}
