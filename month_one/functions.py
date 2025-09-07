def greet():
    print("Hello Akash, welcome to our learning journey!")

greet()

#Functions with Parameters
def greet(name):
    print("Hello", name, "! Let's learn together.")

greet("Gemma")
greet("Akash")

#Functions with return value
def add(a, b):
    return a + b

result = add(5, 7)
print("The sum is:", result)
#Default Parameters
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 3^2 = 9
print(power(3, 3))   # 3^3 = 27 #the default value gets updated if we call with a value

def is_even(num):
   if num % 2 ==0:
       print("True")
   else:
     print("False")
       
       
is_even(2)
is_even(11)
is_even(12) # To check if number given is even
