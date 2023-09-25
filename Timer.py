import time
from os import system, name, path
 
while True:

   if "y" in (choice:=input("Do you want to start? (Y/N)").lower()):
      hours = int(input("Enter the Amount of hours: "))
      minutes = int(input("Enter the Amount of minutes: "))
      secends = int(input("Enter the Amount of secends: "))
      total_time = hours * 3600 + minutes * 60 + secends
      print("The Timer started...")