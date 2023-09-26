import time
from os import system, name, path
 
while True:

   if "y" in (choice:=input("Do you want to start? (Y/N)").lower()):
      hours = int(input("Enter the Amount of hours: "))
      minutes = int(input("Enter the Amount of minutes: "))
      secends = int(input("Enter the Amount of secends: "))
      total_time = hours * 3600 + minutes * 60 + secends
      print("The Timer started...")
      while total_time>=1:
         print(total_time)
         total_time -= 1
         time.sleep(1)
         if name == "nt":
            system("cls")
         else:
            system("clear")