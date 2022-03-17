class Character():
    hp = 0
    damage = 0
    agility = 0
    intelligence = 0
    speed = 0 

    def warrior(self):
        self.hp=120
        self.damage=100
        self.agility=60
        self.intelligence=20
        self.speed=30
        return {'hp':self.hp,'damage':self.damage,'agility':self.agility,'intelligence':self.intelligence,'speed':self.speed}
    
    def wizard(self):
        self.hp=60
        self.damage=140
        self.agility=20
        self.intelligence=100
        self.speed=20
        return {'hp':self.hp,'damage':self.damage,'agility':self.agility,'intelligence':self.intelligence,'speed':self.speed}

    def archer(self):
        self.hp=80
        self.damage=120
        self.agility=80
        self.intelligence=60
        self.speed=50
        return {'hp':self.hp,'damage':self.damage,'agility':self.agility,'intelligence':self.intelligence,'speed':self.speed}

