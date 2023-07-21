import paramiko
import time
import socket

username = 'admin'
password = '70DogB@yU'
switch_with_authentication_issue = []
switch_not_reachable = []

f = open("ip_list.txt")

for line in f.readlines():
    try:
        ip_address = line.strip()
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ip_address,username=username,password=password,look_for_keys=False)
        print ("Successfully connect to ",ip_address)
        command = ssh_client.invoke_shell()
        command.send('sys n\')
        neighbor_list = command.send('dis lldp neighbor list bri n\')
        with open('output.txt', 'w') as file:
            file.write(neighbor_list)
        
