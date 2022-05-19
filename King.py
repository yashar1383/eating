from random import random
#Queen Branch Developed main
class Gubamba():
    List = []
    population = 0
    __stom = 0 
    __childe = 0
    __i : 0
    __j : 0
    def __init__(self,int:Identity) -> None:    #identity -> (selfish,1) , (unselfidh , 0)
        self.state = True   #means alive:True or Death:False
        self.iden = Identity 
        Gubamba.population += 1
        Gubamba.List.append(self)
    def get_identiy(self):
        return self.iden
    def eating(self , eat):
        self.stom = eat
    def move() : #about moving
        pass
class Box():
    price_vale = {0:(1,1) , 1:(1/2,3/2) , 2:(1/2 , 1/2)}
    population = 0
    Idens = 0
    def __init__(self,i,j) -> None:
        self.i = i
        self.j = j
        self.Gubamba = []
        self.fruits = 0
    def add_Gubamba(self , Guba): #Guba is the object 
        if self.fruits == 2 and self.population < 2 :
            self.population += 1
            self.Gubamba.append(Guba)
            self.Idens += Guba.iden
            return True
        else :
            return False
    def add_fruit(self) -> None :
        self.add_fruit = 2
    def feed(self) -> None :
        for Guba in self.Gubamba :
            Guba.eating((self.population -1)*(self.price_vale[self.Idens][Guba.iden]))
    @staticmethod
    def initialization(n,m , t):    
        Map = []
        for j in range(n) : 
            Map.append([])
            for i in range(m) :
                Map[-1].append(Box(j,i))
                if t != 0 and random() < 5:
                    Map[-1][-1].add_fruit()
                    t -= 1
        return Map
Gubamba(0) ; Box(2,3)
for _ in range(10):     #each day
    for _ in range(24): #each hour
        pass
    