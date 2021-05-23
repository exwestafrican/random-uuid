import factory


class RandomGeneratorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = uuid_generator.RandomGenerator
        django_get_or_create = ("id",)
