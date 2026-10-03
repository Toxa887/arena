from abc import ABC, abstractmethod
import time

class Fighter(ABC):
    def __init__(self):
        self.name = input("Введите имя бойца: ")
        self.hp = int(input("HP: "))
        self.attack = int(input("Сила удара: "))
        self.__is_alive = True
        self.__money = 0

    def __add__(self, other: "Fighter"):
        self.name += " " + other.name
        self.hp += other.hp
        self.attack += other.attack
        self.__money += other.__money
        return self

    def __repr__(self):
        return f"{self.name}\nHP: {self.hp}"

    def hit(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.__is_alive = False

    def fight(self, other: "Fighter"):
        while self.hp > 0 and other.hp > 0:
            self.hit(other.attack)
            other.hit(self.attack)
            print(f"{self.name} - HP: {self.hp}")
            print(f"{other.name} - HP: {other.hp}")
            time.sleep(1)
        if self.hp == other.hp: 
            print("Ничья!")
        else: 
            print(self.name if self.hp > other.hp else other.name, "победил!")

    def is_alive(self):
        return self.hp > 0

    @abstractmethod
    def unique_kick(self):
        pass


class Warrior(Fighter):
    def unique_kick(self):
        print("Воин сильно бьет мечом")


class Mage(Fighter):
    def unique_kick(self):
        print("Маг кидает огненный шар")


def remove_dead(players):
    for p in players:
        if not p.is_alive():
            players.remove(p)


players = []
for i in range(2):
    players.append(Warrior())

players[0].fight(players[1])

remove_dead(players)
