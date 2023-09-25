import time
from os import system, name, path
from pydub import AudioSegment
from pydub.playback import play
 
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
      print("Your Time finished...")
      song = AudioSegment.from_mp3(r"\\Timer\Time-Up.mp3")
      print('playing sound using  pydub')
      play(song)

   elif "n" in choice.lower():
      print('''Exiting...
      bye!''')
      break
   else:
      print("Invalid Input!")