from django.test import TestCase

import pytest

from uuid_generator.factories import RandomGeneratorFactory

# Create your tests here.
from uuid_generator.manager import RandomGeneratorDao
from uuid_generator.models import RandomGenerator


def test_generate_uuid(db):
    RandomGeneratorDao.generate_uuid()
    assert RandomGenerator.objects.count() == 1
