import os
from datetime import datetime

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

folderPath = os.path.join(findVolumePath(),f'edna_{datetime.now().strftime("%m%d%Y")}')
os.makedirs(folderPath, exist_ok= True)
print(len(os.listdir(folderPath)))