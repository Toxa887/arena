import time

DEFAULT_HP = 50
DEFAULT_ATTACK = 8

class Fighter:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

def create_fighter():
    name = input("Введите имя бойца: ")
    
    # Если нажать Enter, запишется значение по умолчанию
    hp_input = input(f"HP (по умолчанию {DEFAULT_HP}): ")
    hp = int(hp_input) if hp_input else DEFAULT_HP
    
    attack_input = input(f"Сила удара (по умолчанию {DEFAULT_ATTACK}): ")
    attack = int(attack_input) if attack_input else DEFAULT_ATTACK
    
    return Fighter(name, hp, attack)

def show_players(players):
    for i in range(0, len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")

def fight(a, b):
    while a.hp > 0 and  b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp}")
        print(f"{b.name} - HP: {b.hp}")
        time.sleep(1)
    if a.hp == b.hp: print("Ничья!")
    else: print(a.name if a.hp > b.hp else b.name, "победил!")

def remove_dead(players):
    return [p for p in players if p.hp > 0]

players = []
for i in range(2):
    players.append(create_fighter())
show_players(players)
fight(players[0], players[1])
players = remove_dead(players)
show_players(players)