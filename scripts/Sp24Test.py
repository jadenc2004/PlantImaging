import os
import subprocess
from datetime import datetime
import time

def setCommand(camera: int, path: str, frames=3, brightness=25, contrast=60, exposure=3):
    '''
    sets the command to be executed by subprocess pOpen
    '''
    command = ['sudo',
            'fswebcam',
            '-d', f'/dev/video{camera}',
            '-D', '2',
            '-S', '10',
            '-F', f'{frames}',
            '-r', '3840x2160',
            '-s', f'Brightness={brightness}%',
            '-s', f'Contrast={contrast}%',
            '-s', f'Exposure (Absolute)={exposure}%',
            '-s', 'Backlight Compensation=2',
            '--no-banner',
            f'{path}/images_{camera}_{datetime.now().strftime("%H:%M")}_{brightness}_{contrast}.jpg']
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
	start = time.time()
	volumePath = findVolumePath()
	folderPath = os.path.join(volumePath,f'edna_{datetime.now().strftime("%m%d%Y")}')
	os.makedirs(folderPath,exist_ok=True)
	for i in range(2):
		for j in range(3):
			camera = 2*j
			exposure = 3
			if camera == 4:
				exposure = 1
			mainRun = setCommand(camera=camera,
								path=folderPath,
								exposure=exposure)
			runMainRun = subprocess.Popen(mainRun)
		time.sleep(60)
	print(time.time()-start)

startTest()
