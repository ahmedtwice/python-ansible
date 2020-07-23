#!/usr/bin/python3
# script for web1 server
from pexpect import pxssh

#login to web1
s = pxssh.pxssh()
s.login('192.168.111','justincase','Password01')
print('SSH login successful to web1')

#Add User
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print("Added a new user")

#change password for the user
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print("Password changed successfuly")

# Install Apache (httpd)
s.prompt()
s.sendline('sudo dnf install httpd -y')
print('Apache install success')
s.prompt()
s.sendline('sudo systemctl start httpd')
print('Apache start successufly')
s.prompt()
s.sendline('sudo systemctl enable httpd')
print ('Apache configured to start on boot')

#Firewall Rule
s.prompt()
s.sendline('sudo firewall-cmd --permanent --add-service=http')
s.prompt()
s.sendline('sudo firewall-cmd --reload')
print('Firewall rule added for http')

#logout
s.logout
print("logged out of web1 server")
################################################################
# script for web2 server
from pexpect import pxssh

#login to web2
s = pxssh.pxssh()
s.login('192.168.112','justincase','Password01')
print('SSH login successful to web2')

#Add User
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print("Added a new user")

#change password for the user
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print("Password changed successfuly")

# Install Apache (httpd)
s.prompt()
s.sendline('sudo dnf install httpd -y')
print('Apache install success')
s.prompt()
s.sendline('sudo systemctl start httpd')
print('Apache start successufly')
s.prompt()
s.sendline('sudo systemctl enable httpd')
print ('Apache configured to start on boot')

#Firewall Rule
s.prompt()
s.sendline('sudo firewall-cmd --permanent --add-service=http')
s.prompt()
s.sendline('sudo firewall-cmd --reload')
print('Firewall rule added for http')

#logout
s.logout
print("logged out of web2 server")
###############################################################################################################################################

# script for DB1 server
from pexpect import pxssh

#login to DB1
s = pxssh.pxssh()
s.login('192.168.121','justincase','Password01')
print('SSH login successful to DB1')

#Add User
s.sendline('sudo 1useradd egoad')
s.prompt()
s.sendline('Password01')
print("Added a new user")

#change password for the user
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print("Password changed successfuly")

# Install MariaDB
s.prompt()
s.sendline(' dnf install mariadb mariadb-server -y')
print('MariaDB installed successfuly')
s.prompt()
s.sendline('sudo systemctl start mariadb')
print('MariaDB start successufly')
s.prompt()
s.sendline('sudo systemctl enable mariadb')
print ('MariaDB configured to start on boot')

#logout
s.logout
print("logged out of DB1 server")


##########################################################################################################
# script for DB2 server
from pexpect import pxssh

#login to DB2
s = pxssh.pxssh()
s.login('192.168.122','justincase','Password01')
print('SSH login successful to DB2')

#Add User
s.sendline('sudo useradd egoad')
s.prompt()
s.sendline('Password01')
print("Added a new user")

#change password for the user
s.sendline('sudo passwd egoad')
s.prompt()
s.sendline('RubberDuck!')
s.prompt()
s.sendline('RubberDuck!')
print("Password changed successfuly")

# Install MariaDB
s.prompt()
s.sendline(' dnf install mariadb mariadb-server -y')
print('MariaDB installed successfuly')
s.prompt()
s.sendline('sudo systemctl start mariadb')
print('MariaDB start successufly')
s.prompt()
s.sendline('sudo systemctl enable mariadb')
print ('MariaDB configured to start on boot')

#logout
s.logout
print("logged out of DB2 server")



