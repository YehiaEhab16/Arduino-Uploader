##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# Kernel Functions #

# Importing PySide6 packages
from PySide6.QtCore import QThread, Signal

# Importing required packages
import subprocess, path

# Importing defined modules
from syscom import SerialHandler

# Kernel Handler Class
class KernelHandler(QThread):
    # Emitted signal (kernel text, operation completed)
    KernelOutput = Signal(str,bool)
    
    # Initialize variables
    def __init__(self):
        self.comPort = None
        self.baudRate = None
        self.uploadPath = None
        self.arduinoVersion = None
        super().__init__()
    
    # Get Thread Status
    def isActive(self):
        return not self.comPort == None
    
    # Stop upload upon disconnection
    def interruptUpload(self):
        if self.isActive():
            self.endProcess()
            self.terminate()
    
    # Upload Hex file to arduino
    def upload(self, arduinoVersion:str, baudRate:str, comPort:str, uploadPath:str):     
        # Upload command after specifying comport, version, hexfile and baudrate
        self.comPort = comPort
        self.baudRate = baudRate
        self.uploadPath = uploadPath
        self.arduinoVersion = arduinoVersion
        self.start()

    # Main Thread Fucntion
    def run(self):
        if self.comPort is not None and self.baudRate is not None and self.uploadPath is not None and self.arduinoVersion is not None:
            process = subprocess.Popen(f'{path.PathManager.AvrDudePath} -v {self.arduinoVersion} -P{self.comPort} -b{self.baudRate} -D -Uflash:w:{self.uploadPath}:i', 
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

            # Emit stderr to Main Window
            for line in iter(process.stderr.readline, ''):
                self.KernelOutput.emit(line.strip(), False)

            process.stderr.close()
            process.wait()

            self.endProcess()

    # End Upload
    def endProcess(self):
        # Indicate Output Completion
        self.KernelOutput.emit('', True)
        self.comPort = None
        self.baudRate = None
        self.uploadPath = None
        self.arduinoVersion = None
