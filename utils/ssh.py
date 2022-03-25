# from paramiko import SSHClient

# # Connect
# client = SSHClient()
# client.load_system_host_keys()
# client.connect('challenges.ringzer0team.com', port=10130, username='number', password='Z7IwIMRC2dc764L')
# stdin, stdout, stderr = client.exec_command("ls")
# output = stdout.read()
# print(output)
import pexpect

child = pexpect.spawn("ssh sudoku@challenges.ringzer0team.com -p 10143")
child.expect('password')
child.sendline("dg43zz6R0E")