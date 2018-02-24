import os
import sys
import fileinput
import threading
from threading import Thread
import shutil
import time
import ctypes



a=0
while a<1:
	print('\n\t `.............. `..........`      `.......  .....................`         -:+oossso+/-      ')
	print('\t:hhhhhhhhhhhhhy .hhhhhhhhhhy/`    :hhhhhhh. yhhhhhhhhhhhhhhhhhhhh+      -oyhhhhhhhhhhhhhs:`     ')
	print('\thhhhhhhhhhhhhs `hhhhhhhhhhhhy+`  .hhhhhhh` shhhhhhhhhhhhhhhhhhhh/    -shhhhhhhhhhhhhhhhhhy/    ')
	print('\t-hhhhhhhhhhhhho  yhhhhhhhhhhhhhy+..hhhhhhy  +hhhhhhhhhhhhhhhhhhhh-   /hhhhhhhhhhhhhhhhhhhhhho`  ')
	print('\thhhhhhhhhhhhhh  shhhhhhhhhhhhhhhyohhhhhhs  /hhhhhhhhhhhhhhhhhhhh.  /hhhhhhhhhhhhhhhhhhhhhhhho  ')
	print('\thhhhhhhhhhhhh/  ohhhhhhhhhhhhhhhhhhhhhhho  :hhhhhhhhhhhhhhhhhhhh` .hhhhhhhhhhhhhhhhhhhhhhhhhh: ')
	print('\thhhhhhhhhhhhh:  /hhhhhhhhhhhhhhhhhhhhhhh+  -hhhhhhhhhhhhhhhhhhhy  +hhhhhhhhhhhhhhhhhhhhhhhhhhs ')
	print('\tyhhhhhhhhhhhh-  :hhhhhhhhhhhhhhhhhhhhhhh/  .hhhhhhhhhhhhh....---  shhhhhhhhhhyo//+shhhhhhhhhhh`')
	print('\thhhhhhhhhhhh.  -hhhhhhhhhhhhhhhhhhhhhhh:  `hhhhhhhhhhhhy         yhhhhhhhhhy.    `/hhhhhhhhhh.')
	print('\tohhhhhhhhhhhh.  .hhhhhhhhhhhhhhhhhhhhhhh:  `hhhhhhhhhhhhs         shhhhhhhhh+       yhhhhhhhhh`')
	print('\thhhhhhhhhhhh`  `hhhhhhhhhhhhhhhhhhhhhhh-   yhhhhhhhhhhhs::////`  +hhhhhhhhh/       yhhhhhhhhy ')
	print('\thhhhhhhhhhhh    hhhhhhhooyhhhhhhhhhhhhh.   yhhhhhhhhhhhhhhhhhs   .hhhhhhhhho      .hhhhhhhhh/ ')
	print('\thhhhhhhhhhhy    yhhhhhh: ./oyhhhhhhhhhh.   shhhhhhhhhhhhhhhhh:    +hhhhhhhhh:    .shhhhhhhhs  ')
	print('\thhhhhhhhhhhs    shhhhhh-    ./shhhhhhhh`   ohhhhhhhhhhh/---::`     +hhhhhhhhyo:-/yhhhhhhhhs`  ')
	print('\thhhhhhhhhhhs    ohhhhhh-      `-+yhhhhh`   +hhhhhhhhhhh:            /yhhhhhhhhhhhhhhhhhhho`   ')
	print('\thhhhhhhhhhho    +hhhhhh-         `:oyhh    +hhhhhhhhhhh-             .oyhhhhhhhhhhhhhhhs-     ')
	print('\tsssssssssss/    /ssssss.            .+s    :sssssssssss.               ./syyhhhhhhhys+-`      ')
	print('\t ```````````      ``````               `     ```````````                   `.-:::::-.`         ')
	print('\t`````````` ``````````` ````````````     ``````` ```````` ``````` `````````` ````...````        ')
	print('\t`yyyyyyyyyy:+yyyyyyyyys-yyyyyyyyyyyy- ./osyyhhhh-:yyyyyy/ oyyyyys.yyyyyyyyyy-/hhhhhhhyyso/`     ')
	print('\tshhhhhhyyy./hhhhhhyyyo.yyyhhhhhhyyy./yhhhhhhyyy:-hhhhhh: /hhhhh+ yhhhhhyyyy.:hhhhhhyyhhhhy     ')
	print('\tohhhhho`.. -hhhhhh::/. ```yhhhhy````hhhhhhs:.````hhhhhh- :hhhhh/ yhhhhho::: -hhhhhh--shhhs     ')
	print('\t+hhhhhyss/ .hhhhhy+++`    ohhhhs    +hhhhh/      hhhhhh+oshhhhh: shhhhho++: `hhhhhhoshh+-      ')
	print('\t/hhhhh:``  `hhhhhy+oo:    +hhhh+     -oyhhhso++. yhhhhy`--hhhhh. +hhhhho+oo` hhhhhy:yhhy+.     ')
	print('\t-----`     ---------`    `----`        .-::::-  .----.   -----  .--------.  .----. `/:-`      ')
	print('\n\n\t\t\t\t\t: : : Developed by Sandeep : : :')
	a=a+1
	time.sleep(3) 
os.system('cls')
os.system('color A')
os.system('mkdir basic_info')
os.system('title Info Fetcher')
print('Please wait, we are collecting System Data\n\nPc name...')
os.system('whoami > thispc.txt')
print('Done\n\n\nGetting BIOS info')
os.system('wmic csproduct get name, identifyingnumber > BIOS.txt')
print('Done\n\n\nGetting UUID...')
os.system('wmic path win32_computersystemproduct get uuid > uuid.txt')
print('Done\n\n\nGetting MAC...')
os.system('getmac > mac.txt')
print('Done\n\n\nGetting Internet config...')
os.system('ipconfig > ipconfig.txt')
print('Done\n\n\nGetting System info...')
os.system('systeminfo > systeminfo.txt')
print('Done\n\n\nGetting Drive info...')


def driveD():
	os.system('tree D: /A> basic_info/D.txt')
	

def driveE():
	os.system('tree E: /A> basic_info/E.txt')
	

def driveF():
	os.system('tree F: /A> basic_info/F.txt')
	
def driveG():
	os.system('tree G: /A> basic_info/G.txt')
	



Thread(target = driveD).start()
Thread(target = driveE).start()
Thread(target = driveF).start()
Thread(target = driveG).start()

print('Done\n\n\nClearing Temp Files')
os.system('type thispc.txt BIOS.txt uuid.txt mac.txt systeminfo.txt ipconfig.txt > system.txt')
os.remove('thispc.txt')
os.remove('BIOS.txt')
os.remove('UUID.txt')
os.remove('mac.txt')
os.remove('systeminfo.txt')
os.remove('ipconfig.txt')
os.system('cls')
shutil.move("system.txt", "basic_info/system.txt")
print('\nInformation Fetched Successfully\nin basic_info Folder')


abcd=[]
def func1(abcd):
    os.system('tree D: /A /F > detailed_info/D_drive.txt')
def func2(abcd):
    os.system('tree E: /A /F > detailed_info/E_drive.txt')
def func3(abcd):
    os.system('tree F: /A /F > detailed_info/F_drive.txt')
def func4(abcd):
    os.system('tree G: /A /F > detailed_info/G_drive.txt')


def run():
	if len(abcd)==4:
		input('\nYour Information Saved Successfully in detailed_info Folder\n\n\n\nPress Enter to close program...')

n=input('\n\nDo you want detailed information of your drives(may take time depends on number of files):\nPress 1 if yes: ')
if n==1:
	os.system('mkdir detailed_info')
	Thread(target = func1(abcd)).start()
	run()
	Thread(target = func2(abcd)).start()
	run()
	Thread(target = func3(abcd)).start()
	run()
	Thread(target = func4(abcd)).start()
	run()
if n!=1:
	input('\nYour Information Saved Successfully in detailed_info Folder.\n\n\n\n\nPress Enter to close program...')
