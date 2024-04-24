from datetime import datetime
from enum import Enum
import subprocess
import os

date = datetime.now().strftime("%m%d%Y")

class Pi(Enum):
    '''
    [sourcePath,pw,cameras]
    '''
    NAOMI = [f'pi@raspberrypinaomi.local:/media/pi/DISK2_IMG/naomi_{date}',
             'jennlewis', # replace with pw
            (i*2 for i in range(5))]
    EDNA = [f'pi@raspberrypiEdnaRegina.local:/media/pi/4C28-95CB1/CR_Folder/edna_testStart_{date}',
            'hello', # replace with pw
            (i*2 for i in range(3))]

def transfer(pi):
    source = pi.value[0]
    pw = pi.value[1]
    dest = os.path.join(os.getcwd(),'data') # replace with destination path
    os.makedirs(dest,exist_ok = True)
    subprocess.run(f'sshpass -p {pw} scp -r {source} {dest}', shell=True)

transfer(Pi.EDNA)
