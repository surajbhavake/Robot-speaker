#as I am using ubuntu I have install sudo apt-get install espeak for using it 
#If you are using mac it gives you by default say command you can use that
import os

while True:

    x = input("Enter the text you want to convert to speech for your robot(press q for exit):")
    
    
    if x == 'q':
        os.system("espeak 'Goodbye'")
        break
  
    command = f"espeak '{x}'"
    os.system(command)


