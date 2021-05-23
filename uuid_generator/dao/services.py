from uuid_generator.models import RandomGenerator


class RandomGeneratorService:
    @classmethod
    def generate_uuid(cls):
        return RandomGenerator.objects.create()
