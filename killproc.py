# killproc.py:  List and kill running processes by name or PID
# Author:       David White
# Date:         November 2015

import psutil
import argparse
import sys

def listproc():
    col1 = "Process Name"
    col2 = "PID"
    col3 = "Mem (%)"
    print
    print '%-30s %-8s %s \n' % (col1, col2, col3)
    count = 0
    for proc in psutil.process_iter():
        procname = proc.name()
        procid = str(proc.pid)
        mem = ("%.3f" % proc.memory_percent())
        print '%-30.30s %-8s %s' % (procname, procid, mem,)
        count = count + 1
    print '\n' + str(count) + ' running processes found\n'

def killproc_name(target_process):
    try:
        count = 0
        for proc in psutil.process_iter():
            procname = proc.name()
            if procname == target_process:
                proc.kill()
                count = count + 1
        return count
    except psutil.AccessDenied:
        print "Access Denied - You do not have permission to kill this process\n"
    except:
        print "Error: ", sys.exec_info()[0]
        print "use killproc -h for help\n"

def killproc_PID(target_process):
    try:
        count = 0
        for proc in psutil.process_iter():
            procid = str(proc.pid)
            if procid == target_process:
                proc.kill()
                count = count + 1
        return count
    except psutil.AccessDenied:
         print "Access Denied - You do not have permission to kill this process.\n"
    except:
        print "Error: ", sys.exec_info()[0]
        print "use killproc -h for help.\n"

def main():
    if args.target_PID != None:
        target_PID = args.target_PID
        count = killproc_PID(target_PID)
        if count == 0:
            print "A process with PID %s was not found." % str(target_PID)
        else:
            print "Processes found and killed: " + str(count)
        #print "do stuff with PID's"
    elif args.target_name != None:
        target_name = args.target_name
        count = killproc_name(target_name)
        if count == 0:
            print "Process %s was not found. Note that process name is case sensitive." % target_name
        else:
            print "Processes found and killed: " + str(count) + "\n"
        #print "Do stuff with names"
    else:
        listproc()

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Killproc', description='List and kill running processes by name or PID', epilog='Note Target Name is case sensitive')
    parser.add_argument('-p', '--PID', dest = 'target_PID')
    parser.add_argument('-n', '--name', dest = 'target_name')
    args = parser.parse_args()
    main()
