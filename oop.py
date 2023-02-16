class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age}years old")

#creating an object
myobj=EmobilisStudent("Jeremy",18)
myobj.hello_me()
myobj2=EmobilisStudent("Clarence",21)
myobj2.hello_me()

#create a class call magari,it should have mode,make,year properties
#create min of three objects
class Magari:
    def __init__(self,make,model,year):
        self.model=model
        self.make=make
        self.year=year
    def hello_me(self):
        print(f"The car is a {self.make}. {self.model} of {self.year}")
mycar=Magari("MercedesBenz","A-class",2022)
mycar.hello_me()
mycar=Magari("Audi","A3",2023)
mycar.hello_me()
mycar=Magari("Audi","A4",2023)
mycar.hello_me()


#Another one
class lectures:
    def __init__(self,lecturer,classrep,attedndance):
        self.lecturer=lecturer
        self.classrep=classrep
        self.attendance=attedndance
    def hello_me(self):
        print(f"Today's lecture was precided over by {self.lecturer}.The class rep in attendance was {self.classrep} and attendace was {self.attendance}")
myclasses=lectures("Martin","Aston",87)
myclasses.hello_me()