class Weapon():
    attack = 0
    speed = 0
    range = 0
    weight = 0 
    
    #warrior
    def sword(self):
        self.attack=100
        self.speed=50
        self.range=20
        self.weight=40
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def axe(self):
        self.attack=80
        self.speed=60
        self.range=15
        self.weight=20
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def spear(self):
        self.attack=60
        self.speed=10
        self.range=50
        self.weight=30
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    #wizard
    def fire_wand(self):
        self.attack=200
        self.speed=10
        self.range=50
        self.weight=5
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def wind_wand(self):
        self.attack=50
        self.speed=100
        self.range=50
        self.weight=5
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def lighting_wand(self):
        self.attack=100
        self.speed=50
        self.range=50
        self.weight=5
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    #archer
    def short_bow(self):
        self.attack=100
        self.speed=60
        self.range=100
        self.weight=20
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def long_bow(self):
        self.attack=150
        self.speed=20
        self.range=150
        self.weight=30
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}
    
    def crossbow(self):
        self.attack=200
        self.speed=5
        self.range=150
        self.weight=40
        return {'attack':self.attack,'speed':self.speed,'range':self.range,'weight':self.weight}

