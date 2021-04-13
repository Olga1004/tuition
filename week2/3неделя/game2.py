class Entity():
    def __init__(self, defense, life): # защита. жизнь
        self.defense = defense
        self.life = life


class Predator(Entity):
    def __init__(self, damage, defense, life): # урон
        super().__init__(defense, life)
        self.damage = damage

    def attack(self, score):
        self.life = self.life - score

    def get_life(self):
        return self.life


class Soldier(Predator):
    def __init__(self, firing_range, damage, defense, life): # дальность стрельбы
        super().__init__(damage, defense, life)
        self.firing_range = firing_range

    def attack(self, score):
        if self.firing_range <=1:
            self.life = self.life - score
        else:
            self.life = self.life - score * self.firing_range / 100


class Commander(Soldier):
    def __init__(self, team, firing_range, damage, defense, life):
        super().__init__(firing_range, damage, defense, life)
        self.team = 5

    def attacks(self, score1, score2, score3, score4, score5):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
        self.score5 = score5
        self.life = self.life - (score1+score2+score3+score4+score5+self.damage)

    def get_life(self):
        return self.life


sol1 = Soldier(0, 1000, 1200, 2000)
pred1 = Predator(1100, 800, 2000)
comm = Commander(5, 1, pred1.life, 1500, 2500)
comm.attacks(1200, 200, 300, 400, 500)
print(comm.get_life())
sol1.attack(pred1.damage)
print(sol1.get_life())








