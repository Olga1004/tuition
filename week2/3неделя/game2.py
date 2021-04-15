
class Entity():
    def __init__(self, defense, life): # защита. жизнь
        self.defense = defense
        self.life = life
        self.x = 0
        self.y = 0

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def get_defense(self):
        return self.defense


class Predator(Entity):
    def __init__(self, damage, defense, life): # урон
        super().__init__(defense, life)
        self.damage = damage

    @property
    def total_damage(self):
        return self.damage

    def attack(self, target, coord_x, coord_y):
        if target.x == coord_x and target.y == coord_y:
            if self.total_damage < target.defense:
                target.defense = target.defense - self.total_damage
                print('Вы поранили цель')
            else:
                target.defense = 0
                target.life = target.life - (self.total_damage - target.defense)
                print('Вы отняли всю защиту у соперника')
            return target.life <= 0
        print('Вы промахнулись')
        return False


class Soldier(Predator):
    def __init__(self, firing_range, damage, defense, life):
        super().__init__(damage, defense, life)
        self.firing_range = firing_range

    def is_in_range(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5 < self.firing_range

    @property
    def total_damage(self):
        if not is_in_range:
            return 0
        return self.damage


class Commander(Soldier):
    def __init__(self, firing_range, damage, defense, life, team:Soldier):
        super().__init__(firing_range, damage, defense, life)
        self.team = team

    @property
    def total_damage(self):
        return super().total_damage + sum(
            [soldier.total_damage for soldier in team],
            0
        )

# sol1 = Soldier(1, 20, 160, 300)
# sol1.location(10, 20)
# pred1 = Predator(25, 200, 500)
# pred1.location(10, 15)
# sol1.attack(pred1, 10, 15)
# print(pred1.get_defense())
# pred1.attack(sol1, 10, 20)
# print(sol1.get_defense())
# comm1 = Commander(10, 30, 180, 350, sol1)
# comm1.attack(pred1, 10, 15)
# print(pred1.get_defense())







