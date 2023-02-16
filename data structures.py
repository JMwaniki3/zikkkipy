#list in python
myclassmate=["Erick", "Joan", "Michael", "victor"]
myclassmate[0]='Sylvia'
myclassmate.append("Daniel")
myclassmate.insert(2, "Christine")
myclassmate.append("James")
myclassmate.insert(0, "Martin")
myclassmate.sort()
print(type(myclassmate))
print(myclassmate)
print(myclassmate[1])
print("My name is "+myclassmate[4])

#Tuple in python
myfavfruits=("Mangoes", "Apples", "Pineapples")
print(myfavfruits)
print(myfavfruits[0])
mynos=[3,7,9,2,6,0,8]
mynos.sort()

#sets datastructures
myfavcars={"Toyota","Mercedes","Nissan","Volkswagen"}
myfavcars.add("peugot")
print(myfavcars)

#dictionaries in python
magari={
    "Name":"Toyota",
    "model": "Premio",
    "year": 2020
}
print(magari)
print(magari["model"])
