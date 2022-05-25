from random import random
# end import
#start body
class Gubamba():
    List = []
    population = [0,0]
    state = False #does the Box that object is in has food
    __belly = 0 #number of foods in Guba belly
    __childe = 0 #number of childs Guba has
    __i : 0 #Gubamba location(x)
    __j : 0 #Gubamba location(y)
    def __init__(self, Identity : int , belly = 0) -> None:    #identity -> (selfish,1) , (unselfidh , 0)
        self.state = True   #means alive:True or Death:False
        self.iden = Identity  #selfish:1 & unselfidh:0
        self.__belly = belly #new childe
        Gubamba.population[Identity] += 1
        Gubamba.List.append(self)
    def get_identiy(self):
        return self.iden
    def eating(self , eat:int ):
        self.__belly = eat
    def live_Division(self): #from conditions make decision of living or creating a child
        if self.__belly == 2 :
            self.__childe += 1
            Gubamba.population += 1
            Gubamba.list.append(Gubamba(self.iden , belly=1))
        if self.__belly == 3/2 and random() < 0.5 : #if under 0.5 breath a child else do nithing
            self.__childe += 1
            Gubamba.population += 1
            Gubamba.list.append(Gubamba(self.iden , belly = 1))
        elif self.__belly == 1/2 and random() < 0.5 :  #if under 0.5 die
            del Gubamba.List[Gubamba.List.index(self)]
            Gubamba.population -= 1
        elif  self.__belly == 1 : 
            del Gubamba.List[Gubamba.List.index(self)]
            Gubamba.population -= 1
    def Housing(self): #the Box that Guba is in , has food
        self.state = True
    def move(self) : #about moving
        if self.state == False: #if Guba was in Box without food
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
    def Guba_enter(self):
        global Map
        if Map[self.__j , self.__i].add_Gibamba(self) :
            self.state = True
        else :
            self.state = False # for each day when the Boxes changes the stable situation would disappeared
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
            self.Idens += Guba.get_identiy()
            return True
        else :
            return False
    def add_fruit(self) -> None :
        self.fruits = 2
    def feed(self) -> None :
        for Guba in self.Gubambas :
            Guba.eating(self.price_vale[self.population -1][Guba.iden])
    @staticmethod
    def initialization(n,m , t):    
        Map = []
        for j in range(n) : #j:y , i:x
            Map.append([])
            for i in range(m) :
                Map[-1].append(Box(j,i))
                if t != 0 and random() < 5:
                    Map[-1][-1].add_fruit()
                    t -= 1
        return Map
n , m , t= int(input()) , int(input()) , int(input()) # t: number of foods
x , y = int(input('unselfish : ')) , int(input('selfish :'))
for _ in range(x):
    Gubamba(0)
for _ in range(y):
    Gubamba(1)
for _ in range(10):     #each day4
    Map = Box.initialization(n ,m ,t )
    for _ in range(24): #each hour
        for Guba in Gubamba.List :
            Guba.Guba_enter()
            Guba.move()
    for box in Map :
        box.feed()
    for Guba in Gubamba.list :
        Guba.live_Division()
    