##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# GUI Main #

# Importing PySide6 Packages
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QLabel
from PySide6.QtGui import QPixmap, QIcon, QMovie
from PySide6.QtCore import QPropertyAnimation

# Importing Required Packages
import sys

# Importing Defined Packages
from syscall import KernelHandler
from syscom import SerialHandler
from server import ServerHandler
from path import PathManager
from gui import ArduinoUI

# Main Window Class
class ArduinoUploader(QWidget):
    def __init__(self):
        # Initialize UI
        super().__init__()
        sys.excepthook = lambda excType, excValue, _ : QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{excType.__name__}: {excValue}")
        self.ui = ArduinoUI()  # Save the instance of ArduinoUI to self.ui
        self.ui.setupUi(self)
        self.centerWindow()

        # Serial variables
        self.comPort = ''
        self.arduinoVersion = '-patmega328p -carduino'  # Arduino uno
        self.baudRate = '115200'

        # Progress Update
        self.dotCount  = 0
        self.progress   = 0
        self.stepSize  = 0
        self.totalSize = 0
        self.ui.progressBar.setValue(0)      
        
        # Create Animations
        self.progressAnimation = QPropertyAnimation(self.ui.progressBar, b"value")
        self.progressAnimation.setDuration(250)
        self.showAnimation(PathManager.LoadingGifPath, self.ui.topAnimation)
        self.showAnimation(PathManager.RndGifPath, self.ui.bottomAnimation)

        # Kernel Thread Initialize
        self.kernelThread = KernelHandler()
        self.kernelThread.KernelOutput.connect(self.Handle_Output)

        # Serial Thread Initialize
        self.serialThread = SerialHandler()
        self.serialThread.ConnectedPort.connect(self.Handle_Serial)

        # Server Initialize
        self.serverThread = ServerHandler()
        self.serverThread.VersionStatus.connect(self.Handle_Version)
        self.serverThread.UpdateStatus.connect(self.Handle_State)
        self.serverThread.UpdateSize.connect(self.Hanle_Size)
            
        # Initialize Buttons
        self.Handle_Buttons()
           
    # GUI buttons
    def Handle_Buttons(self):
        self.ui.projectButton1.clicked.connect(lambda: self.Handle_Project('Project1'))   # Project Button 1
        self.ui.projectButton2.clicked.connect(lambda: self.Handle_Project('Project2'))   # Project Button 2
        self.ui.projectButton3.clicked.connect(lambda: self.Handle_Project('Project3'))   # Project Button 3
        self.ui.projectButton4.clicked.connect(lambda: self.Handle_Project('Project4'))   # Project Button 4
        self.ui.projectButton5.clicked.connect(lambda: self.Handle_Project('Project5'))   # Project Button 5
        self.ui.eraseButton.clicked.connect(lambda: self.Handle_Project('Erase'))         # Erase Button 
        self.ui.blinkButton.clicked.connect(lambda: self.Handle_Project('Blink'))         # Blink Test Button
        self.ui.hexButton.clicked.connect(self.Handle_Browse)                             # Browse Button  
        self.ui.updateButton.clicked.connect(self.Handle_Update)                          # Refresh Button  
        self.ui.projectSelector.currentChanged.connect(self.Handle_Index)                 # Project Selector Tool Box

    # Center GUI in screen
    def centerWindow(self):
        window = self.frameGeometry()
        window.moveCenter(self.screen().availableGeometry().center())
        self.move(window.topLeft())

    # Show animations
    def showAnimation(self, gif:str, label:QLabel):
        animatedIcon = QMovie(gif)
        animatedIcon.setScaledSize(label.size())
        label.setMovie(animatedIcon)
        animatedIcon.start()

    # Handle Kernel Thread Output
    def Handle_Output(self, output:str, isCompleted:bool):
        self.ui.projectSelector.setCurrentIndex(3)
        if isCompleted:
            if '\n'.join(self.recievedText.split('\n')[-3:-1]) == 'avrdude: safemode: Fuses OK (E:00, H:00, L:00)\navrdude done.  Thank you.':
                QMessageBox.information(self,'Done Uploading', 'Code uploaded to arduino successfully')
            else:
                QMessageBox.warning(self,'Upload Error', 'Error occured while uploading\nPlease check arduino connection and try again')
            self.Handle_Serial(self.comPort)
        else:
            if output != '':
                self.recievedText += f'{output}\n'
                self.ui.outputUpload.setText(f'{self.recievedText}\n\n')
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

    # Get size of update
    def Hanle_Size(self, size:int):
        self.totalSize = size
        self.stepSize = 100 / size      

    # Get latest version
    def Handle_Version(self, version:dict):
        if version != ServerHandler.VersionNetworkError:
            self.showAnimation(PathManager.WifiGifPath, self.ui.topAnimation)
            if version != ServerHandler.VersionNotFound:
                self.ui.updateButton.setIcon(QIcon(PathManager.NotificationPngPath))
        else:
            self.showAnimation(PathManager.NoWifiGifPath, self.ui.topAnimation)
        
    # Display server feedback
    def Handle_State(self, state:int):
        if state == ServerHandler.ServerNetworkError:
            QMessageBox.warning(self, 'Download Error', 'Error while downloading new files\nPlease check your internet connection and try again')
            self.showAnimation(PathManager.NoWifiGifPath, self.ui.topAnimation)
            self.Handle_Serial(self.comPort)
        elif state == ServerHandler.ServerUpdateComplete:
            QMessageBox.information(self, 'Download Completed', 'All firmware files were updated successfully')
            self.Handle_Serial(self.comPort)
            self.ui.updateButton.setIcon(QIcon(PathManager.UpdatePngPath))
            
            self.showAnimation(PathManager.WifiGifPath, self.ui.topAnimation)

            self.progress = 0
            self.ui.progressBar.setValue(self.progress)

        elif state == ServerHandler.ServerInProgress:
            # Ensure the progress does not exceed 100
            targetProgress = min(100, self.progress + self.stepSize)

            # Set animation parameters based on current and target progress
            self.progressAnimation.setStartValue(self.ui.progressBar.value())
            self.progressAnimation.setEndValue(targetProgress)

            # Start the animation
            self.progressAnimation.start()

            # Update internal progress for future calculations
            self.progress = targetProgress

            # Determine the percentage progress
            percent = int(self.progress)

            # Create the text for the label
            dots = '.' * (self.dotCount % 3 + 1)  
            self.dotCount += 1
            self.ui.portLabel.setText(f"Updating {percent}% {dots}")

        elif state == ServerHandler.ServerLatestFiles:
            self.Handle_Serial(self.comPort)
            self.showAnimation(PathManager.WifiGifPath, self.ui.topAnimation)
            QMessageBox.information(self, 'Update Notification', 'Latest update already installed')
            
        elif state == ServerHandler.ServerVersionComplete:
            self.ui.portLabel.setText("Updating 100% ...")
            self.progress = 0
            self.ui.progressBar.setValue(self.progress)

    # Update labels when connecting to serial port
    def Handle_Serial(self, port:str):               
        self.comPort = port
        if self.comPort == SerialHandler.NoDeviceFound:
            self.ui.portLabel.setText(self.comPort)
            self.ui.portLabel.setStyleSheet('border-bottom: 2px solid red;')
            self.ui.connectionLabel.setPixmap(QPixmap(PathManager.RedPngPath))
            self.kernelThread.interruptUpload()
        else:
            self.ui.portLabel.setText('Connected: ' + self.comPort)
            self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(90,225,110);')
            self.ui.connectionLabel.setPixmap(QPixmap(PathManager.GreenPngPath))          

    # Update Hex files from server
    def Handle_Update(self):
        self.showAnimation(PathManager.DownloadGifPath, self.ui.topAnimation)
        self.ui.portLabel.setText("Connecting to Server...")
        self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
        self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
        self.serverThread.checkUpdates()

    # Upload new hex file
    def uploadHexFile(self, hexFile:str):
        # Upload hex file
        if self.comPort != SerialHandler.NoDeviceFound:
            # Arduino Uno Check
            if self.ui.unoRadio.isChecked():
                # Set version and baud rate
                self.arduinoVersion = '-patmega328p -carduino'
                self.baudRate = '115200'
                # Check for hex file availability
                if hexFile in self.serverThread.getFiles(ServerHandler.BoardUno):
                    self.recievedText = ''
                    self.ui.portLabel.setText(f'Uploading to {self.comPort}')
                    self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
                    self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
                    self.kernelThread.upload(self.arduinoVersion, self.baudRate, self.comPort, PathManager.UnoFilesPath + hexFile)
                    
                else:
                    QMessageBox.information(self, 'Upload Error', 'No hex file provided for this board')
            # Arduino Mango Check
            elif self.ui.mangoRadio.isChecked():
                # Set version and baud rate
                self.arduinoVersion = '-patmega328p -carduino'
                self.baudRate = '115200'
                # Check for hex file availability
                if hexFile in self.serverThread.getFiles(ServerHandler.BoardMango):
                    self.recievedText = ''
                    self.ui.portLabel.setText(f'Uploading to {self.comPort}')
                    self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
                    self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
                    self.kernelThread.upload(self.arduinoVersion, self.baudRate, self.comPort, PathManager.MangoFilesPath + hexFile)
                else:
                    QMessageBox.information(self, 'Upload Error', 'No hex file provided for this board')

            # Arduino Mega Check
            elif self.ui.megaRadio.isChecked():
                # Set version and baud rate
                self.arduinoVersion = '-patmega2560 -cwiring'
                self.baudRate = '115200'
                # Check for hex file availability
                if hexFile in self.serverThread.getFiles(ServerHandler.BoardMega):
                    self.recievedText = ''
                    self.ui.portLabel.setText(f'Uploading to {self.comPort}')
                    self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
                    self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
                    self.kernelThread.upload(self.arduinoVersion, self.baudRate, self.comPort, PathManager.MegaFilesPath + hexFile)
                else:
                    QMessageBox.information(self, 'Upload Error', 'No hex file provided for this board')
            # Arduino Nano Check
            elif self.ui.nanoRadio.isChecked():
                # Set version and baud rate
                self.arduinoVersion = '-patmega328p -carduino'
                self.baudRate = '57600'
                # Check for hex file availability
                if hexFile in self.serverThread.getFiles(ServerHandler.BoardNano):
                    self.recievedText = ''
                    self.ui.portLabel.setText(f'Uploading to {self.comPort}')
                    self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
                    self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
                    self.kernelThread.upload(self.arduinoVersion, self.baudRate, self.comPort, PathManager.NanoFilesPath + hexFile)
                else:
                    QMessageBox.information(self, 'Upload Error', 'No hex file provided for this board')
            else:
                QMessageBox.warning(self, 'No Board Selected', 'No board Selected\nPlease select the required board first')
        else:
            QMessageBox.warning(self, 'Arduino Not Connected', 'No serial device detected\nPlease connect the required board first')

    # Upload Project
    def Handle_Project(self, project:str):
        self.uploadHexFile(PathManager.getHexFile(project))

    # Handle Index Change
    def Handle_Index(self, _):
        if not self.kernelThread.isActive():
            self.ui.outputUpload.setText('')        

    # Browse new hex file
    def Handle_Browse(self):
        if self.comPort != SerialHandler.NoDeviceFound:
            # Arduino Check
            if self.ui.unoRadio.isChecked() or self.ui.mangoRadio.isChecked(): 
                self.arduinoVersion = '-patmega328p -carduino'
                self.baudRate = '115200'
            elif self.ui.megaRadio.isChecked():
                self.arduinoVersion = '-patmega2560 -cwiring'
                self.baudRate = '115200'
            elif self.ui.nanoRadio.isChecked():
                self.arduinoVersion = '-patmega328p -carduino'
                self.baudRate = '57600'
            else:
                QMessageBox.warning(self, 'No Board Selected', 'No board Selected\nPlease select the required board first')

            if self.ui.unoRadio.isChecked() or self.ui.mangoRadio.isChecked() or self.ui.megaRadio.isChecked() or self.ui.nanoRadio.isChecked():
                hexFileDirectory = QFileDialog.getOpenFileName(self, caption="Choose Hex File to Upload", directory=".", filter="Hex File (*.hex)")[0]

                # Check for hex file path
                if hexFileDirectory != '':
                    self.recievedText = ''
                    self.ui.portLabel.setText(f'Uploading to {self.comPort}')
                    self.ui.portLabel.setStyleSheet('border-bottom: 2px solid rgb(250,150,0);')
                    self.ui.connectionLabel.setPixmap(QPixmap(PathManager.LoadingPngPath))
                    self.kernelThread.upload(self.arduinoVersion, self.baudRate, self.comPort, hexFileDirectory)
        else:
            QMessageBox.warning(self, 'Arduino Not Connected', 'No serial device detected\nPlease connect the required board first')
    
    # Overriding close event to dispose camera
    def closeEvent(self, event):
        self.serialThread.terminate()
        self.serverThread.terminate()
        self.kernelThread.terminate()
        event.accept()

# Executing GUI
if __name__ == '__main__':  
    app = QApplication(sys.argv)
    ArduinoUploader().show()
    app.exec()
  