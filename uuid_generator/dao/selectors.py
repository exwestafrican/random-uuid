from uuid_generator.models import RandomGenerator


class RandomGeneratorSelector:
    @classmethod
    def fetch_all_uuids(cls):
        return RandomGenerator.objects.all()
