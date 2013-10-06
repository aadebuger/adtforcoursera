'''
Created on 2013-10-1

@author: aadebuger
'''
import os
import sys
from pyadb import ADB
def  pushfile(file):
    adb = ADB('/Users/aadebuger/Documents/android-sdk-mac_x86/platform-tools/adb') 
    print adb.pyadb_version()
    aa =adb.push_local_file(file, "storage/sdcard0/coursera"+"/")
#    aa=adb.shell_command("""push "%s" storage/sdcard0/coursera"""%(file))
    print 'lines=',aa    
def  copyfile(file,remotedir):
    print 'copyfile=',file,remotedir
    adb = ADB('/Users/aadebuger/Documents/android-sdk-mac_x86/platform-tools/adb') 
    print adb.pyadb_version()
    aa =adb.push_local_file(file, remotedir)
#    aa=adb.shell_command("""push "%s" storage/sdcard0/coursera"""%(file))
    print 'copyfile lines=',aa   
def  mkdir(dir):
    adb = ADB('/Users/aadebuger/Documents/android-sdk-mac_x86/platform-tools/adb') 
    print adb.pyadb_version()
    adb.shell_command("mkdir %s"%(dir))
def pushdir(dir):
#    files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    print "listdir=",os.listdir( dir )
    for f in os.listdir(dir):
        print 'f=',f,os.path.isfile(os.path.abspath(f)),os.path.isdir(os.path.abspath(f))
        print 'abspath=',os.path.abspath(f)
        pushfile(os.path.abspath(f))
    files = filter(os.path.isfile, os.listdir( dir ) )

    print files
    for f in files:
        print f
def copyDir(dir,remotedir):
   print 'dir=',dir
   for f in os.listdir(dir):
        print 'f=',f,os.path.isfile(f),os.path.isdir(f)
        if f==".DS_Store":
            print 'find .DS_Store'
        else:
            splitname = os.path.splitext(f)
            print "splitname=",splitname

            if splitname[1]!='':
                copyfile(dir+'/'+f,remotedir)
                print 'file='               
            else:
                print 'dir='
                newremotedir = remotedir+"/"+ f
                print 'newdir=',newremotedir
                mkdir(newremotedir)
                copyDir(dir+"/"+f ,newremotedir)
  
def getSection(dir):
    print "listdir=",os.listdir( dir )
    retv=[]
    for f in os.listdir(dir):
        print 'f=',f,os.path.isfile(f),os.path.isdir(f)
        if f==".DS_Store":
            print 'find .DS_Store'
        else:
            retv.append(f)

            
if __name__ == '__main__':
#    mkdir("progfun-003")
#    pushfile("/Users/aadebuger/Documents/github/coursera/progfun-003/03_Week_2-_Higher_Order_Functions/01_Lecture_2.1_-_Higher-Order_Functions.mp4")
#    pushdir("/Users/aadebuger/Documents/github/coursera/progfun-003/03_Week_2-_Higher_Order_Functions");
#    pushdir("/Users/aadebuger/Documents/github/coursera/progfun-003");
#    getSection("/Users/aadebuger/Documents/github/coursera/progfun-003")
#     copyDir("/Users/aadebuger/Documents/github/coursera/progfun-003","storage/sdcard0/coursera/progfun-003")
#     mkdir("storage/sdcard0/coursera/bigdata-003")
#     copyDir("/Users/aadebuger/Documents/github/coursera/bigdata-003","storage/sdcard0/coursera/bigdata-003")
    if len(sys.argv)>=2:
        mkdir("storage/sdcard0/coursera/"+ sys.argv[1])
        copyDir("/Users/aadebuger/Documents/github/coursera/"+sys.argv[1],"storage/sdcard0/coursera/"+sys.argv[1])
    else:
       print ' python pushtosdcard.py  localdir'