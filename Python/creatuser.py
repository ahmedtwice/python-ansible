#!/usr/bin/python3
# Logs into WEB and DB servers and creats username and password  

import pexpect

def CreateUser(ipAddr):
    # open connection and login
    child = pexpect.spawn('ssh justincase@' + ipAddr)
    child.expect('justincase.* password:')
    child.sendline('Password01')
    print('Logged in')

    #crate username and password:
    child.expect('\[justincase@.*\]\$')
    child.sendline('sudo su -')
    child.expect('/[sudo\] password for justincase:')
    child.sendline('Password01')
    child.expect('\[root@.*\]\#')
    child.sendline('useradd egoad')
    child.expect('\[root@.*\]\#')
    child.sendline('passwd egoad')
    child.expect('Changing password for user egoad.\n New password:')
    child.sendline('RubberDuck!')
    child.expect('BAD PASSWORD: The password fails the dictionary check - it is based on a dictionary word\n Retype new password:')
    child.sendline('RubberDuck!')
    print("created new username and password")

#logout
    child.expect('passwd: all authentication tokens updated successfully.\n\\[root@.*\]\#')
    child.sendline('exit')
    child.expect('\[justincase@.*\]\$')
    child.sendline('exit')
    print("logged out")
Addresses = ['192.168.0.111','192.168.0.112', '192.168.0.121','192.168.0.122']
for address in Addresses:
    CreateUser(address)

