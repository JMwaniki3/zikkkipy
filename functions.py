#
def hello():
    print("This is my first function")
hello()
def calculate():
    x=9
    y=8
    print(x*y)
calculate()
def majina(firstname, lastname):
    print(firstname+""+lastname)
majina("Jeremy", "Michael")
majina("Christine", "Michael")
majina("John", "Grisham")
def greetings(name, greeting="Hello"):
    print(greeting +""+ name)
greetings(" Jeremy")
greetings("Joan","Niaje")
def location(name, locat1on="Where are you?"):
    print(name +""+ locat1on)
location("Jeremy.")
#maximum value func
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,9,8,1,17,45)
print(result)
#minimum value func
def minvalue(z,y,x,w,v,u):
    return min(z,y,x,w,v,u)
result=minvalue(78,89,5,7,78,53)
print(result)
#tuple func
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4,2])
print(answer)
#func to print out nos.
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(5)