import os
import subprocess
from datetime import datetime
import time

def setCommand(camera: int, path: str, idx: int, frames=3, brightness=0, contrast=60, focus = 98):
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
            f'{path}/images_{camera}_{datetime.now().strftime("%H:%M")}_{idx}.jpg']
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
    volumePath = findVolumePath()
    folderPath = os.path.join(volumePath,f'edna_{datetime.now().strftime("%m%d%Y")}')
    os.makedirs(folderPath,exist_ok=True)
    for i in range(20):
        for j in range(3):
            camera = 2*j
            mainRun = setCommand(camera=camera,
                                 path=folderPath,
                                 idx= i)
            subprocess.Popen(mainRun)
        time.sleep(2)
startTest()
