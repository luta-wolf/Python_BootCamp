'''
super().__init__() - базовый (родительский) класс с помощью которого мы можем
вызывать методы и обращиться к полям родительского класса
'''

from collections import Counter
from Player import Player


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player):

        for _ in range(self.matches):
            p1_puts = player1.put_candy()
            p2_puts = player2.put_candy()
            # print(player1.name, p1_puts)
            # print(player2.name, p2_puts)

            if p1_puts and p2_puts:
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
                player1.get_candy(2)
                player2.get_candy(2)
            elif p1_puts and (not p2_puts):
                self.registry[player1.name] -= 1
                self.registry[player2.name] += 3
                player1.get_candy(0)
                player2.get_candy(3)
            elif (not p1_puts) and p2_puts:
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
                player1.get_candy(3)
                player2.get_candy(0)
            elif (not p1_puts) and (not p2_puts):
                player1.get_candy(0)
                player2.get_candy(0)
            # print(player1.name, self.registry[player1.name])
            # print(player2.name, self.registry[player2.name])
            # print('-----------------------------------------------------------------')

    def top3(self):
        for name, score in self.registry.most_common(3):
            print(f"{name} {score}")
