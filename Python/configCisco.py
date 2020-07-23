#!/usr/bin/python3
# Expect script using pxssh

from pexpect import pxssh

# create session and login
s = pxssh.pxssh()
s.login('cisco@192.168.0.11','cisco')
print('SSH login successful')

# Send command
s.sendline('conf t', 'int g2', 'ip add 192.168.1.12 255.255.255.0', 'no shut')
s.prompt()
print(s.before)

# logout
s.logout()
                    
