#1.We have the following student details and marks enter these details from the keyboard
#student name = Ritah Liz
#student number = SEP23/BCS/14
#Programmming = 78
#Data science = 89
#Computer applications = 55
#Calculate the average mark and print the number in 3 decimal places.

#2. Write a program that converts celcius temperature to fahrenheit, the program should ask a user to enter the temperature in degrees celcius and display the temperature in fahrenheit.
#farenheit = (celcius * 9/5) + 32


#3. A car's mile per gallaton can be calcuated with the following formula; miles driven/ gallons of car used.
#.Write the program that asks the user for the no. of miles driven and gallons used.
#It should calculate the cars miles and display the results.

#1.
student_name = (input("Enter the student name: "))
student_number =(input("Enter the student number: "))
programming = int(input("Enter the marks attained in Programming : "))
data_science = int(input("Enter the marks attained in Data science: "))
computer_applications = int(input("Enter the marks attained in Computer applications: "))

total_sum = programming + data_science + computer_applications
print(f"The  sum is {total_sum}")
number = 3
average_mark = total_sum / number
print(f"The average mark is {average_mark:.3f}")
#average_mark = round(total_sum / number,3)


#3
miles_driven = float(input("Enter the miles driven: "))
gallons_used = float(input("Enter the amount of gallons used: "))
mpg = miles_driven / gallons_used
print(f"The number of miles driven per gallons used is {mpg:.2f}")

#2
temperature = int(input("Enter temperature in °C: "))
fahrenheit_temperature = (9/5) * temperature + 32
print(f"The temperature in °F is {fahrenheit_temperature:.3f}")





