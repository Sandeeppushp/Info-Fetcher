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
	os.system('tree D: > basic_info/D.txt')
	f1 = open('basic_info/D.txt', 'r')
	f2 = open('basic_info/temp.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÃÄÄÄ', ''))
	f1 = open('basic_info/temp.txt', 'r')
	f2 = open('basic_info/D.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÀÄÄÄ', ''))
	f1 = open('basic_info/D.txt', 'r')
	f2 = open('basic_info/temp.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1 = open('basic_info/temp.txt', 'r')
	f2 = open('basic_info/D.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1.close()
	f2.close()
	os.remove('basic_info/temp.txt')

def driveE():
	os.system('tree E: > basic_info/E.txt')
	f1 = open('basic_info/E.txt', 'r')
	f2 = open('basic_info/temp2.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÃÄÄÄ', ''))
	f1 = open('basic_info/temp2.txt', 'r')
	f2 = open('basic_info/E.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÀÄÄÄ', ''))
	f1 = open('basic_info/E.txt', 'r')
	f2 = open('basic_info/temp2.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1 = open('basic_info/temp2.txt', 'r')
	f2 = open('basic_info/E.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1.close()
	f2.close()
	os.remove('basic_info/temp2.txt')

def driveF():
	os.system('tree F: > basic_info/F.txt')
	f1 = open('basic_info/F.txt', 'r')
	f2 = open('basic_info/temp3.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÃÄÄÄ', ''))
	f1 = open('basic_info/temp3.txt', 'r')
	f2 = open('basic_info/F.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÀÄÄÄ', ''))
	f1 = open('basic_info/F.txt', 'r')
	f2 = open('basic_info/temp3.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1 = open('basic_info/temp3.txt', 'r')
	f2 = open('basic_info/F.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1.close()
	f2.close()
	os.remove('basic_info/temp3.txt')

def driveG():
	os.system('tree G: > basic_info/G.txt')
	f1 = open('basic_info/G.txt', 'r')
	f2 = open('basic_info/temp4.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÃÄÄÄ', ''))
	f1 = open('basic_info/temp4.txt', 'r')
	f2 = open('basic_info/G.txt', 'w')
	for line in f1:
	    f2.write(line.replace('ÀÄÄÄ', ''))
	f1 = open('basic_info/G.txt', 'r')
	f2 = open('basic_info/temp4.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1 = open('basic_info/temp4.txt', 'r')
	f2 = open('basic_info/G.txt', 'w')
	for line in f1:
	    f2.write(line.replace('³', '.'))
	f1.close()
	f2.close()
	os.remove('basic_info/temp4.txt')



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
    a = open("detailed_info/D_drive.txt", "w")
    for path, subdirs, files in os.walk(r'D:\\'):
       for filename in files:
          f = os.path.join(path, filename)
          a.write(str(f) + os.linesep)
    return abcd.append(1)
def func2(abcd):
    
    a = open("detailed_info/E_drive.txt", "w")
    for path, subdirs, files in os.walk(r'E:\\'):
       for filename in files:
          f = os.path.join(path, filename)
          a.write(str(f) + os.linesep)
    return abcd.append(2)
def func3(abcd):
   
    a = open("detailed_info/F_drive.txt", "w")
    for path, subdirs, files in os.walk(r'F:\\'):
       for filename in files:
          f = os.path.join(path, filename)
          a.write(str(f) + os.linesep)
    return abcd.append(3)

def func4(abcd):
    a = open("detailed_info/G_drive.txt", "w")
    for path, subdirs, files in os.walk(r'G:\\'):
       for filename in files:
          f = os.path.join(path, filename)
          a.write(str(f) + os.linesep)
    return abcd.append(4)


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
