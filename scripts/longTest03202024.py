import os
import subprocess
from datetime import datetime
import time

def setCommand(camera: int, path: str, frames=3, brightness=0, contrast=60, focus = 98):
    '''
    sets the command to be executed by subprocess pOpen
    '''
    if (camera == 2):
        brightness = 16
        contrast = 64
    command = ['sudo',
            'fswebcam',
            '-d', f'/dev/video{camera}',
            '-D', '2',
            '-S', '10',
            '-F', f'{frames}',
            '-r', '3840x2160',
            '-s', f'Brightness={brightness}%',
            '-s', f'Contrast={contrast}%',
            '-s', f'Focus (absolute)={focus}%',
            '-s', 'Backlight Compensation=2',
            '--no-banner',
            f'{path}/images_{datetime.now().strftime("%H:%M")}.jpg']
    return command

def findVolumePath():
    '''
    finds the volume that is connected on the device then it tries to
    find CR_Folder, if it is not there it will make the folder, if the volume isn't even in, then it will just return the Documents
    folder native to the pi
    '''
    mediaPath = "/media/pi/"
    USBPath = os.listdir(mediaPath)
    if USBPath != []:
        volumePath = os.path.join(mediaPath,USBPath[0], "CR_Folder")
        if (os.path.exists(volumePath) == False):
            os.makedirs(volumePath)
        return volumePath
    else:
        return "/home/pi/Documents/"

def startTest():
    start = time.now()
    volumePath = findVolumePath()
    folderPath = os.path.join(volumePath,f'edna_testStart_{datetime.now().strftime("%m%d%Y")}')
    cameraPaths = []
    for i in range(3):
        path = os.path.join(folderPath, f'camera_{2*i}', exist_ok=True)
        cameraPaths.append(path)
        os.makedirs(path, exist_ok=True)
    while (time.now() - start < 60*60*24*5): # 5 day trial
        for j in range(3):
            camera = 2*j
            mainRun = setCommand(camera=camera,
                                 path=cameraPaths[j])
            subprocess.Popen(mainRun)
        time.sleep(60*10) # every 10 mins

startTest()
