##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# Serial Functions #

# Importing Required Packages
from PySide6.QtCore import QThread, Signal
import serial.tools.list_ports as serial

# Serial handler class
class SerialHandler(QThread):
    # Signal to notify about arduino connection
    ConnectedPort = Signal(str)
    # Connection feedback
    NoDeviceFound = 'Arduino Not Connected'
    
    # Class constructor
    def __init__(self):
        super().__init__()
        self.previousPort = None
        self.threadActive = False
        self.start()

    # Main thread loop
    def run(self):
        self.threadActive = True
        while self.threadActive:
            port = self.listen()
            if port != self.previousPort:
                self.ConnectedPort.emit(port)
                self.previousPort = port

    # Listen to connected ports
    def listen(self) -> str:
        # Read connected serial ports
        ports = serial.comports()
        # Loop on all ports
        for port in ports:
            port = str(port)
            port = port.split(' - ')
            if 'ch340' in port[1].lower() or 'arduino' in port[1].lower():
                return port[0]
        # In case of no devices found
        return self.NoDeviceFound
    
    # Terminate thread
    def terminate(self):
        self.threadActive = False
        super().terminate()
