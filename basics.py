#Getting started - hello world

print ("Hello world")

print ("How can I write a comment?") # the text after the pound sign is ignored

# This is a comment, which can document what your program does or leave a note for another user

# Anything after the # is ignored by python. 

print ("I could have code like this.") # and the comment after it is ignored 
    
# You can also use a comment to "disable" or comment out a piece of code:    

print ("This won't run.")
print ("This will run.")



# PART 1: NUMBERS AND MATH

print (1+1)

print (1+1,2+2,3+3)

print ("what is 3 plus 2?", 3+2)

print ("Is it true that 3 + 2 < 5 - 7?")

print (3+2<5-7)
print (3+2>5-7)



#PRACTICE

#Write a program to print your name and city of residence on one line

print ("Name: Sanjay Lote, City of residence: Mumbai")

#Write a program to calculate the sum of 1234 and 5678

x = 1234
y = 5678
sum = x+y
print (sum)

#Alternate way:

print (1234+5678)

# PART 2: VARIABLES AND NAMES

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = space_in_a_car * cars_driven
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")


#PRACTICE: Calculate your BMI Formula: 703 x weight (lbs) / [height (in)]^2

weight= 135
height= 70

BMI= (703 * weight / (height)**2)

print (BMI)

#EXERCISE THREE: IF AND ELSE STATEMENTS


#If statements

people = 20
cats = 30
dogs = 15

if people < cats:
    print ("Too many cats!")

if people > cats:
    print ("Not enough cats!")

if people < dogs:
    print ("Too many dogs!")

if people > dogs:
    print ("Not enough dogs!")


dogs = dogs + 5

if people > dogs:
    print ("People outnumber dogs.")

if people < dogs:
    print ("Dogs outnumber people.")

if people == dogs:
    print ("A dog for everyone.")



#If, else if (elif), and else
    
people = 30
cars = 40
buses = 15


if cars > people:
 print ("We should take the cars.")
elif cars < people:
   print ("We should not take the cars.")
else:
    print ("We can't decide.")

if buses > cars:
    print ("That's too many buses.")
elif buses < cars:
    print ("Maybe we could take the buses.")
else:
    print ("We still can't decide.")

if people > buses:
    print ("Alright, let's just take the buses.")
else:
     print ("Fine, let's stay home then.")














