import os
import subprocess


command = ["ls", "-la"]


def run_command(command):

    output = subprocess.run(command, capture_output=True, text=True)
    return output


output = run_command(command)

#print(f"{command} Return code:--> ", output.returncode)

print(output.stdout)