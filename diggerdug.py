#!/usr/bin/env python3

import subprocess
import time


print (50 * '#')
print (50 * '-')
print ("             WELCOME TO DIGGER-DUG")
print (50 * '-')
print (50 * '#')
time.sleep(1)
print ("MIT License, v. 1.1")
time.sleep(1)
print()

def main():
    host = str(input("Enter the URL:  "))

    subprocess.call(['dig', '@8.8.8.8', host])
    
    
    print("Run DIG against a different DNS?")

    choice = input("yes or no?  ").lower()
    
    if choice.startswith('y'):

       subprocess.call(['dig', '@1.1.1.1', host])
       

       print("Maybe one more DNS for good measure??")

       choice = input("yes or no?  ").lower()
       if choice.startswith('y'):
     
          subprocess.call(['dig', '@169.57.122.145', host])
          

       print("Would you like me to check the host with nmap?") 
       nmap = input("yes or no?  ").lower()
       if nmap.startswith('y'):

          subprocess.call(['nmap', '-Pn', host])
          
       print()
       print("I can also check the host with netcat. Would you like me to run that now?")
       nc = input("yes or no?  ").lower()
       if nc.startswith('y'):
      
          port = str(input("Enter the port you need to check:  "))
          subprocess.call(['ncat', '-v', '-z', '-w 3', host, port])

       time.sleep(1)
       print()
       print("All done!")


       if choice.startswith('n'):
         print ("Goodbye!")

    else:
        
       print ("Goodbye!")

    
main()
