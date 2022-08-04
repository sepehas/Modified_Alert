import os.path
import time
from playsound import playsound #pip install playsound
from datetime import datetime

class Checker:
    
    def __init__(self, FILE, DRIVE_PATH = None):
        if not DRIVE_PATH:
            self.DRIVE_PATH = "G:/_ModifiedAlert/Files/" #DEFAULT Path
        else: 
            self.DRIVE_PATH = DRIVE_PATH

        self.FILE = FILE
        self.FILE_NAME = self.FILE[0]
        self.STOP_HOUR = self.FILE[1]
        self.START_TIME = time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(os.path.getmtime(self.DRIVE_PATH + self.FILE_NAME)))
        self.Checked = False


    def checkModified(self, fileName = ""):
    
        currentTime = time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(os.path.getmtime(self.DRIVE_PATH + self.FILE_NAME)))
        print(f"Checking file {fileName}, last modified: {self.START_TIME}")

        if self.START_TIME != currentTime:
            
            self.START_TIME = time.strftime("%d/%m/%Y %H:%M:%S", time.gmtime(os.path.getmtime(self.DRIVE_PATH + self.FILE_NAME)))
            
            print(f'File {fileName} was modified')  
            self.Checked = True 
            

    def start(self):
            self.checkModified(self.FILE_NAME)



ALERT_PATH = "G:/_ModifiedAlert/alert.wav"
FILES_TO_CHECK = []
INTERVAL = 3

files = [["1.txt","15"],["2.txt","15"],["3.txt","15","G:/_ModifiedAlert/Files/"],["4.txt","15"]]
#files = [["File name.txt", "last hour", "drive path"], ... , ...]

def fileList(fileName, stopHour, drivePath): #Structure files 
    files.append([fileName,stopHour,drivePath])
    return files

def doStuffWhenModified(file):
    playsound(ALERT_PATH)
    time.sleep(1)
    os.startfile(file.DRIVE_PATH + file.FILE_NAME) #open FILE



for file in files:
    try:
        FILES_TO_CHECK.append(Checker(file))

    except Exception as e:
            print(f"Exception: {e} for file: {file[0]}")
            continue
while len(FILES_TO_CHECK):
    print(f"{len(FILES_TO_CHECK)} Files Left")
    for file in FILES_TO_CHECK:
        date = datetime.now()
        now = date.strftime("%H")

        if int(now) >= int(file.STOP_HOUR):
            print(f"Hour Limit exceded for file: {file.FILE_NAME}")
            continue
        else:
            if not file.Checked:
                file.start()

            else:
                doStuffWhenModified(file)
                FILES_TO_CHECK.remove(file)

    print("----------------")
    time.sleep(INTERVAL)

print("All files have been modified!")
