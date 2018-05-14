# Digger Dug

A python script for checking hosts

## What it does

Digger Dug will run a dig command up to three times using 3 different DNS's; yes, there are times that may be needed. 

Once completed, it will ask you if you would like to check the host using `nmap` (must be installed on your system--unless using snap*). The full command is `nmap -Pn` so as to simply check which ports are open as there are times during trouble-shooting a host's issues that knowing which ports are open or closed can lead to a better outcome. 

It will then ask if you'd like to run `netcat` (full command is `netcat -z -v - w 3`) and which port you'd like to check. 

It will complete each task and print results as you go along. 

A `snap` will be available, soon. 

## To run 

`python diggerdug.py`

or you can copy it to `/bin (or other)` and run `sudo chmod +x diggerdug.py` to make it executable without the need to call up `python` every time. 
