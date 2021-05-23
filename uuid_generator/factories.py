import factory


class RandomGenerator(factory.django.DjangoModelFactory):
    class Meta:
        model = uuid_generator.RandomGenerator
        django_get_or_create = ("id",)
