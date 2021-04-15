
class Entity():
    def __init__(self, defense, life): # защита. жизнь
        self.defense = defense
        self.life = life


class Predator(Entity):
    def __init__(self, damage, defense, life): # урон
        super().__init__(defense, life)
        self.damage = damage

    def attack(self, target, coord_x, coord_y):
        if target.x == coord_x and target.y == coord_y:
            if self.damage < target.defense:
                target.defense = target.defense - self.damage
                print('Вы поранили цель')
            else:
                target.defense = 0
                target.life = target.life - (self.damage - target.defense)
                print('Вы отняли всю защиту у соперника')
        else:
            print('Вы промахнулись')

    def location(self, x, y):
        self.x = x
        self.y = y

    def get_defense(self):
        return self.defense


class Soldier(Predator):
    def __init__(self, firing_range, damage, defense, life):
        super().__init__(damage, defense, life)
        self.firing_range = firing_range


class Commander(Soldier):
    def __init__(self, firing_range, damage, defense, life, sold):
        super().__init__(firing_range, damage, defense, life)
        self.team = input('Введите имена солдат через запятую: ').split(',')
        self.sold = sold

    def attack(self, target, coord_x, coord_y):
        if target.x == coord_x and target.y == coord_y:
            if self.damage + len(self.team) * self.sold.damage < target.defense:
                target.defense = target.defense - (self.damage + len(self.team) * self.sold.damage)
                print('Вы поранили цель')
            else:
                target.defense = 0
                target.life = target.life - (self.damage + len(self.team) * self.sold.damage - target.defence)
                print('Вы отняли всю защиту у соперника')
        else:
            print('Вы не попали в соперника')


sol1 = Soldier(1, 20, 160, 300)
sol1.location(10, 20)
pred1 = Predator(25, 200, 500)
pred1.location(10, 15)
sol1.attack(pred1, 10, 15)
print(pred1.get_defense())
pred1.attack(sol1, 10, 20)
print(sol1.get_defense())
comm1 = Commander(10, 30, 180, 350, sol1)
comm1.attack(pred1, 10, 15)
print(pred1.get_defense())







