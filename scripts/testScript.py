import os
import subprocess
import time
import shlex

pw = 'hello'
pwAuth = f'sshpass -p "{pw}"'
script = 'paramTest03182024.py'

def filecounter():
    command = 'sudo python3 countCurrentTest.py'
    output = subprocess.check_output(shlex.split(f'{pwAuth} ssh pi@raspberrypiednaregina.local "{command}"'))
    return int(output.decode("utf-8"))

def start():
    subprocess.run(f'{pwAuth} scp scripts/{script} pi@raspberrypiednaregina.local:~/Sp24Scripts', shell= True)
    sshCommand = f'sudo python3 Sp24Scripts/{script}; disown top; exit'
    command = shlex.split(f'{pwAuth} ssh pi@raspberrypiednaregina.local {sshCommand}')
    capture = subprocess.Popen(command)
    while capture.poll() is None:
        time.sleep(1)
    print("exited")
    subprocess.run('python3 scripts/fileTransfer.py', shell= True)

start()
