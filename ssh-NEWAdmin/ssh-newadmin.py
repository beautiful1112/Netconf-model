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
        cmdlist = open(cmd.txt,'r')
        cmdlist.seek(0)
        for cmdline in cmdlist.readlines():
        command.send(cmdline+'n\')
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535)
        print(output.decode('ASCII'))

    except paramiko.ssh_exception.AuthenticationException:
        print('User authentication failed for ' + ip)
        switch_with_authentication_issue.append(ip)
    except socket.error:
        print(ip + 'is not reachable')
        switch_not_reachable.append(ip)

f.close()
ssh_client.close

print('\nUser authentication failed for below switches:')
for i in switch_with_authentication_issue:
    print(i)
print('Below switches are not reachable')
for i in switch_not_reachable:
    print(i)


