class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def take_damage(self, damage):
        self.health -= max(damage - self.defense, 0)
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def attack_player(self, other_player):
        damage = self.attack
        print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        other_player.take_damage(damage)
class Drakon(Player):
    def __init__(self, name, health, attack, defense ,flight):
        super().__init__(name, health, attack, defense)
      #  super().__init__(health)
       # super().__init__(attack)
       # super().__init__(defense)    
        self.flight = flight
    
    def fly(self, flight):
       # fly = self.flight
        print("Дракон взлетел вверх")
        if (knight1.health >= 0 and knight2.health > 0 and knight3.health > 0):
            Drakon.attack_player(knight1)
        elif knight2.health > 0 and knight3.health > 0:
            Drakon.attack_player(knight2)
        else:
            Drakon.attack_player(knight3)
        #flight=flight-1
# Create instances of players
knight1 = Player("Player 1", 100, 10, 5)
knight2 = Player("Player 2", 120, 8, 7)
knight3 = Player("Player 3", 100, 20, 7)
Drakon = Drakon("Drakon", 100, 30, 7, 20)
x=6 
# Game logic
while ((knight1.health > 0 or knight2.health > 0 
or knight3.health > 0) 
and Drakon.health > 0) :
    if ((Drakon.flight % 2== 0) and (Drakon.flight > 0)) :
        Drakon.fly(Drakon.flight)            
    else:  
        if (knight1.health >= 0 and knight2.health > 0 and knight3.health > 0):
            
            knight3.attack_player(Drakon)
            knight1.attack_player(Drakon)
            knight2.attack_player(Drakon)
            Drakon.attack_player(knight1)
        elif knight2.health > 0 and knight3.health > 0:
            knight3.attack_player(Drakon)
            knight2.attack_player(Drakon)
            Drakon.attack_player(knight2)
        else:
            knight3.attack_player(Drakon)
            Drakon.attack_player(knight3)
    
    Drakon.flight=Drakon.flight-1
# Determine the winner
if Drakon.health >= 0:
    print(f"Победил {Drakon.name} , все рыцари погибли")
    print(f" Жизнь дракона = {Drakon.health} ")
elif knight1.health >= 0 and knight2.health >= 0 and knight3.health >= 0:
    print(f"Победили рыцари погиб {Drakon.name}")
    print(f" Жизнь рыцаря 1 = {knight1.health} ")
    print(f" Жизнь рыцаря 2 = {knight2.health} ")
    print(f" Жизнь рыцаря 3 = {knight3.health} ")
elif knight2.health >= 0 and knight3.health >= 0:
    print(f"Победили рыцари погибли {Drakon.name} и {knight1.name}")
    print(f" Жизнь рыцаря 2 = {knight2.health} ")
    print(f" Жизнь рыцаря 3 = {knight3.health} ")
else:
    print(f"Победили рыцари выжил только {knight3.name}")
    
    print(f" Жизнь рыцаря 3 = {knight3.health} ")
    