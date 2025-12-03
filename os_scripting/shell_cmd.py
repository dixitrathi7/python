import os
import subprocess


command = ["ls", "-la"]

#subprocess.run(["echo", "hello world from India"])

#output = subprocess.run(["ls", "-la"])  this will print the output on the console where you run code
output = subprocess.run(command, capture_output=True, text=True)

print(f"{command} Return code:--> ", output.returncode)

print(output.stdout)