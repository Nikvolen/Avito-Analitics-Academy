import random
from abc import ABC, abstractmethod


class AnimeMon(ABC):

    @property
    @abstractmethod
    def exp(self):
        pass

    @abstractmethod
    def inc_exp(self, val):
        pass


class Pokemon(AnimeMon):

    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value):
        self._exp += value + 1337

    def __str__(self):
        return self.name


class Digimon(AnimeMon):

    def __init__(self, name):
        self.name = name
        self._exp = 0

    @property
    def exp(self):
        return self._exp

    def inc_exp(self, value):
        self._exp += value * 133

    def __str__(self):
        return self.name


def train(pokemon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    pika = Pokemon(name='Pikachu')
    rimuru = Digimon(name='Rimuru')

    train(pika)
    print(f'Pokemon {pika} gain: {pika.exp} exp')

    train(rimuru)
    print(f'Digimon {rimuru} gain: {rimuru.exp} exp')