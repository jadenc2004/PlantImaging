import time
import subprocess
import os

def callibration_test():
    cwd = os.getcwd()
    imgpath = '/media/pi/DISK_IMG2/plants_03042024'
    os.chdir(imgpath)
    CAMERAS = [i+5 for i in range(5)]
    print(CAMERAS)
    focus = 600
    for camera in CAMERAS:
        print("Camera ", camera)
        focus = 600
        while focus <= 700:
            af = f'sudo v4l2-ctl -d /dev/video{camera} -c "backlight_compensation"=2 -c "auto_exposure"=3 -c "contrast"=32 -c "brightness"=32 -c "focus_absolute"={focus}'
            result=subprocess.run(af,shell=True)
            time.sleep(1)
            takepicture = f"gst-launch-1.0 v4l2src device=/dev/video{camera} num-buffers=1 ! image/jpeg,width=3264,height=2448 ! jpegparse ! filesink location=video{camera}_focus_{focus}.jpg"
            result=subprocess.run(takepicture,shell=True)
            time.sleep(1)
            print("Focus ", focus)
            if not os.path.isfile(f"{imgpath}/video{camera}_focus_{focus}.jpg"):
                print("error")
                break
            focus += 20
    os.chdir(cwd)

'''
    Retrieve a given v4l2 control value
'''
def get_control(device_path, control_name):
    command = f"v4l2-ctl -d {device_path} --get-ctrl={control_name}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Error: {result.stderr}"
    
def output_control(device_path, control_name):
    initial_control, new_control = get_control(camera_device, control_name), get_control(camera_device, control_name)
    start, current_time = time.time(), time.time()
    period = 20  # 10 seconds
    while (current_time - start < period):
         new_control = get_control(camera_device, control_name)
         print(f"{control_name} (initial, new): {initial_control} {new_control}")
         current_time = time.time()
    print(f"TIME TAKEN TO SWITCH BACK TO INITIAL: {current_time - start}") 

# Example usage
camera_device = "/dev/video4"
control_name = "focus_absolute"

#output_control(camera_device, control_name)


callibration_test()
