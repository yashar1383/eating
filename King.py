from random import random
# end import
#start body
class Gubamba():
    List = []
    population = 0
    state = False #does the Box that object is in has food
    __belly = 0 #number of foods in Guba belly
    __childe = 0 #number of childs Guba has
    __i : 0 #Gubamba location(x)
    __j : 0 #Gubamba location(y)
    def __init__(self,int:Identity) -> None:    #identity -> (selfish,1) , (unselfidh , 0)
        self.state = True   #means alive:True or Death:False
        self.iden = Identity  #selfish:1 & unselfidh:0
        Gubamba.population += 1
        Gubamba.List.append(self)
    def get_identiy(self):
        return self.iden
    def eating(self , eat):
        self.belly = eat
    def live_Division(self): #from conditions make decision of living or creating a child
        if self.belly == 2 :
            self.__childe += 1
            Gubamba.population += 1
            Gubamba.list.append(Gubamba(self.iden))
        if self.belly == 3/2 and random() < 0.5 : #if under 0.5 breath a child else do nithing
            self.__childe += 1
            Gubamba.population += 1
            Gubamba.list.append(Gubamba(self.iden))
        elif self.belly == 1/2 and random() < 0.5 :  #if under 0.5 die
            del Gubamba.List[Gubamba.List.index(self)]
            Gubamba.population -= 1
        elif  self.belly == 1 : 
            del Gubamba.List[Gubamba.List.index(self)]
            Gubamba.population -= 1
    def Housing(self): #the Box that Guba is in , has food
        self.state = True
    def move(self) : #about moving
        if self.state == False:
            if random() > 0.5:
                if random() > 0.5:
                    self.__i = (self.__i + 1)%m
                else :
                    self.__i = (self.__i +m - 1)%m
            else :
                if random() > 0.5:
                    self.__j = (self.__j + 1)%n
                else :
                    self.__j = (self.__j +n - 1)%n
class Box():
    price_vale = {0:(1,1) , 1:(1 /2,3/2) , 2:(1/2 , 1/2)}
    population = 0
    Idens = 0
    def __init__(self,i,j) -> None:
        self.i = i #direction i
        self.j = j #diraction j (of Box)
        self.Gubambas = [] #list of human in it
        self.fruits = 0 #number of fruit in 
    def add_Gubamba(self , Guba : Gubamba): #add guba in Box if conditions return True (Guba is the object )
        if self.fruits == 2 and self.population < 2 :
            self.population += 1
            self.Gubambas.append(Guba)
            self.Idens += Guba.iden
            return True
        else :
            return False
    def add_fruit(self) -> None :
        self.add_fruit = 2
    def feed(self) -> None :
        for Guba in self.Gubambas :
            Guba.eating(self.price_vale[self.population -1][Guba.iden])
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
n , m = int(input()) , int(input())
for _ in range(10):     #each day
    for _ in range(24): #each hour
        pass
    