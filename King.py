from random import random
# end import
#start body
class Gubamba():
    List = []
    population = [0,0]
    def __init__(self, Identity : int , belly = 0) -> None:    #identity -> (selfish,1) , (unselfidh , 0)
        self. state = False #does the Box that object is in has food
        self. __belly = 0 #number of foods in Guba belly
        self. __childe = 0 #number of childs Guba has
        self. __i = 0+(m-1)*(1-Identity) #Gubamba location(x)
        self. __j = 0+(n-1)*(1-Identity) #Gubamba location(y)
        self.state = True   #means alive:True or Death:False
        self.iden = Identity  #selfish:1 & unselfidh:0
        self.__belly = belly #new childe
        self.deth_alive = True
        Gubamba.population[Identity] += 1
        Gubamba.List.append(self)
        #print(len(Gubamba.List) , sum(self.population))
    def get_identiy(self):
        return self.iden
    def eating(self , eat:int ):
        self.__belly = eat
    def live_Division(self): #from conditions make decision of living or creating a child
        if self.__belly == 2 :
            self.__childe += 1
            Gubamba.List.append(Gubamba(self.iden , belly=1))
        elif self.__belly == 3/2 and random() < 0.5 : #if under 0.5 breath a child else do nithing
            self.__childe += 1
            Gubamba.List.append(Gubamba(self.iden , belly = 1))
        elif self.__belly == 1/2 and random() < 0.5 :  #if under 0.5 die
            self.deth_alive = False
            Gubamba.population[self.iden] -= 1
            #print(len(Gubamba.List) , sum(self.population)) just for debug
        elif  self.__belly == 1 : 
            self.deth_alive = False
            Gubamba.population[self.iden] -= 1
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
        if Map[self.__j][self.__i].add_Gubamba(self) :
            self.state = True
        else :
            self.state = False # for each day when the Boxes changes the stable situation would disappeared
class Box():
    price_vale = {0:(1,1) , 1:(1 /2,3/2) , 2:(1/2 , 1/2)}
    def __init__(self,i,j) -> None:
        self.population = 0
        self.Idens = 0
        self.i = i #direction i
        self.j = j #diraction j (of Box)
        self.Gubambas = [] #list of human in it
        self.fruits = 0 #number of fruit in 
    #def show (self):
    #    return f"|f:{self.fruits},G{self.population}|"
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
                if t != 0 and random() < 0.5:
                    Map[-1][-1].add_fruit()
                    t -= 1
        return Map
#def Show_status(d=0,h=0): #for showing visual map
#   print(f'day : {d} \ hour : {h}')
#   for i in Map :
#       for j in i :
#           print(j.show(),end=' ')
#       print()
n , m , t= int(input('n: ')) , int(input('m: ')) , int(input('t: ')) # t: number of foods
x , y = int(input('unselfish : ')) , int(input('selfish :'))
for _ in range(x):
    Gubamba(0)
for _ in range(y):
    Gubamba(1)
for jp in range(10):     #each day 24 loop
    Map = Box.initialization(n ,m ,t )
    for ip in range(60): #each hour
        for Guba in Gubamba.List :
            if Guba.deth_alive :
                Guba.Guba_enter()
                Guba.move()
    for col in Map :
        for box in col:
            box.feed()
    for Guba in Gubamba.List :
        if Guba.deth_alive :
            Guba.live_Division()
    del Map
    print(f"All population : {sum(Gubamba.population)}")
    print(f"Selfish : {Gubamba.population[1]}   | Unselfish : {Gubamba.population[0]}")