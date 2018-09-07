#!/usr/bin/env python

import os
import subprocess
import sys
if __name__=='__main__':
    #Variables to store the source and destination
    #files/folders size in order to compare them
    sourceSize = []
    destinationSize = []
    #takes the input from command line
    #for Example # python sync.py /u01/files/a.mp4
    source = str(sys.argv[1])
    #The Folder Name of Destination should be excluded in order to
    #Prevent unecessary sync Operation
    folder = os.path.basename(source)
    #some unnecessray print commands
    #print(source)
    #print(folder)
    #Calculating Source File/Folder size
    testExistance = os.system('du -sh ' + source + ' > /dev/null 2>&1')
    if(testExistance != 0):
        print('file not found')
        sys.exit()
    sourceSizeProc = subprocess.Popen(['du','-sh',source], stdout=subprocess.PIPE)
    sourceSize = sourceSizeProc.communicate()[0].split('\t')
    #Obtaining the destination Directory by replacing part of
    #source Path with "/content"
    destination = source.replace([Source-Directory],[Destination-Directory])
    #Calculating Destination File/Folder size
    destSizeProc = subprocess.Popen(['ssh', '-p 2222', 'root@Destination-ip', 'du', '-sh', destination], stdout=subprocess.PIPE)
    destinationSize = destSizeProc.communicate()[0].split('\t')
    destination = destination.replace(folder,'')
    #print(destination)
    if(sourceSize[0] == destinationSize[0]):
        print(1)
    elif(sourceSize[0] != destinationSize[0]):
        #checking if the file is being synchronized
        syncProcPipe1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
        syncProcPipe2 = subprocess.Popen(['grep', 'rsync'], stdin=syncProcPipe1.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        syncProcPipe3 =  subprocess.Popen(['grep', source], stdin=syncProcPipe2.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        syncStat = syncProcPipe3.communicate()[0].split('\t')
        #if len(syncStat[0]) is greater than zero, it means that 
		#an rsync process is being executed in memory
        if(len(syncStat[0]) == 0):
                print(0)
                cmd='until rsync --ignore-existing --recursive --progress --partial-dir=.rsync-partial \
				--timeout=30 -v -e "ssh -p2222" '+ source + ' Destination-ip:'+ destination + ' ; do \
				echo Tansfer disrupted, retrying in 2 seconds...;   sleep 2; done'
				#executes the rsync in the background
				 subprocess.Popen(cmd, bufsize=0, shell=True, stdout=subprocess.PIPE)
        else:
			#value 2 indicates that the file/directory is being synchronized
                print(2)

