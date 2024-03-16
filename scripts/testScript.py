import os
import subprocess
import time

pw = 'hello'
pwAuth = f'sshpass -p {pw}'

def filecounter():
    command = 'sudo python3 countCurrentTest.py'
    return (int) subprocess.check_output(f'{pwAuth} ssh pi@raspberrypiednaregina.local {command}')

def start():
    pw = 'hello'
    init_fc = filecounter()
    sshCommand = 'sudo python3 Sp24Test.py; exit'
    command = shlex.split(f'{pwAuth} ssh pi@raspberrypiednaregina.local {command}')
    capture = subprocess.POpen(command)
    for i in range(1):    
        time.sleep(60)
        if filecounter() == init_fc:
            print('error')
            capture.kill()
            subprocess.run('python3 fileTransfer.py')
    subprocess.run('python3 fileTransfer.py')

cwd = os.getcwd()
os.chdir('~/School/Sp24/PIPackage')
start()
os.chdir(cwd)
