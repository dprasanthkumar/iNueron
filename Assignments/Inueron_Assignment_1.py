#1.Find out all the types of error that we have encountered in our lecture and why? Also include the examples.

#FIRST
TEN = 10
ten = 20
# TEN and ten both are different in terms of lowercase and uppercase letter
print(Ten)

#Justification:We haven't defines the variable "Ten" so that it will through the error.

#SECOND

print = "Hi there" # as a variable
type(print)
print("Hi there")

#TypeError: 'str' object is not callable

#**Justification**:fist print is defined as a variable so we connot take again a variable as a function.

#THIRD
name = input("Name: ") # always gives you string values
place = input("place: ")
year_of_birth = input("year_of_birth: ")

age = 2022 - year_of_birth
print(f"""
My name is: {name}
I live at: {place}
{name} is of age: {age}
""")

''' **justification**:we have to define year_of_birth data type to integer as below
year_of_birth = int(input("year_of_birth: ")) '''




#2.Take input A and B and print their sum, mul, div, square of the nos.
#Ans:
A = int(input("Enter you first number: "))
B = int(input("Enter your second number: "))

print(f"Sum of A and B => {A} + {B}=", (A + B))
print(f"product of A and B => {A}*{B}=", (A * B))
print(f"division of A and B => {A}%{B}=", (A % B))
print(f"square of A and B => {A}**{B}=", (A ** B))




#3.How many reserve keywords are there in python and why we should not use them as a variable name.

#Ans:
'''
Reserved words (also called keywords) are defined with predefined meaning and syntax in the language. These keywords have to be used to develop programming instructions. 
Reserved words can’t be used as identifiers for other programming elements like name of variable, function etc.

Following is the list of reserved keywords in Python 3
and
except
lambda
with
as
finally
nonlocal
while
assert
false
None
yield
break
for
not
class
from
or
continue
global
pass
def
if
raise
del
import
return
elif
in
True
else
is
try
Python 3 has 33 keywords while Python 2 has 30. The print has been removed from Python 2 as keyword and included as built-in function.
'''



#4.Create email ids with the user inputs. in the following format - lastname.firstname@gmail.com

#Ans:

last_name=input("Enter Your last name:")
first_name=input("Enter your firstname:")

print(f"Mail_id: {last_name}.{first_name}@gmail.com")










'''5.Try to print the following lines -
Hi I'm Sunny
My address is 22\3
I earn 20$ daily.'''

#Ans:
print("""Hi I'm Sunny
My address is 22\3
I earn 20$ daily.""")


# 6.Take user input (name, address, date of birth etc) to fill a form for your college and print their email IDs

#Ans:
name = input("Enter your Name:")
DOB = input("enter your date of birth in format(YYYY-MM-DD):")
address = input("Enter your address:")
mail_id = input("Enter tour email_id:")
print(f"your mail_id is :{mail_id}")

'''7.Convert the following -
"22.4" into integer
"22" into complex no.'''

Ans:
a=(22.4)
b=(22)
print(int(a))
print(complex(b))