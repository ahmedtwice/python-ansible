#!/usr/bin/python3
# Logs into remote system and runs the hostname command 

import pexpect

def GetHostname(ipAddr):
    # open connection and login
    child = pexpect.spawn('ssh justincase@' + ipAddr)
    child.expect('justincase.* password:')
    child.sendline('Password01')
    print('Logged in')

    #send host name commance:
    child.expect('\[justincase@.*\]\$')
    child.sendline('hostname')
    print("got hosname")
    
    #logout
    child.expect('\[justincase@.*\]\$')
    print(child.before)
    child.sendline('exit')
    print("logged out")
GetHostname('192.168.0.111')

