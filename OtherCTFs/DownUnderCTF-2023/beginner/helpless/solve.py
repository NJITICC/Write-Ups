import paramiko

# Set up SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace with your server details
hostname = "2023.ductf.dev"
port = 30022
username = "ductf"
password = "ductf"

# Connect to the remote server
ssh.connect(hostname, port=port, username=username, password=password)

# Replace with the remote file path you want to retrieve
remote_file_path = "/home/ductf/flag.txt"

# Replace with the local file path where you want to save the retrieved file
local_file_path = "./flag.txt"

# Retrieve the file
sftp = ssh.open_sftp()
sftp.get(remote_file_path, local_file_path)
sftp.close()

# Close the SSH connection
ssh.close()

print(f"File '{remote_file_path}' retrieved and saved as '{local_file_path}'")
