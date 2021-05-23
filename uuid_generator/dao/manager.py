from uuid_generator.doa.selectors import RandomGeneratorSelector
from uuid_generator.doa.services import RandomGeneratorService


class RandomGeneratorDao(RandomGeneratorSelector, RandomGeneratorService):
    pass
