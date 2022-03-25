from paramiko import SSHClient

# Connect
client = SSHClient()
client.load_system_host_keys()
client.connect('challenges.ringzer0team.com', port=10130, username='number', password='Z7IwIMRC2dc764L')
stdin, stdout, stderr = client.exec_command("ls")
output = stdout.read()
print(output)