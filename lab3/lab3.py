#python class 4460 <-- this is a comment
print("hello world")
a = 5 
b = 6

print(a+b)

#var name rules --> a != A
#naming conventions
#use descriptive names
#use lowercase letters
#use underscores between words

varsity_avg_gpa = 1.5

print(type(varsity_avg_gpa))
#literal usage
print(type(4.0))
#operators
#assignment is =
#arithmetic
#comparison <>==
#logical and or not
# can use += instead of x = x + 1

#string concatenation
name = "ken"

print("my name is " + name +", not barbie")

print(f"my name is {name}, not barbie")

#variable typing

number = 999 * 10

print(str(number)[0:3])


def numbers(a,b):
  output = a + b
  return output
print(numbers(1,2))
def add_numbers(a,b):
  print(a+b)
  print(b)
  #print(P)
print(add_numbers(2,4))


#variable scope

name = "Ken"

def say_hello():
  name = "Barbie"
  return f"hello {name}"

print(say_hello())
print(name)