from uuid_generator.dao.selectors import RandomGeneratorSelector
from uuid_generator.dao.services import RandomGeneratorService


class RandomGeneratorDao(RandomGeneratorSelector, RandomGeneratorService):
    pass
