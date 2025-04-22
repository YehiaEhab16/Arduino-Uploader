##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# Server Functions #

# Importing PySide6 Packages
from PySide6.QtCore import QThread,Signal

# Importing Requied Packages
import pyrebase, requests, os

# Importing Defined Packages
from config import FirebaseCredentials
from path import PathManager

# Server Handler Class
class ServerHandler(QThread):
    # Emitted Signals
    VersionStatus = Signal(dict)
    UpdateStatus  = Signal(int)
    UpdateSize    = Signal(int)

    # Server States
    ServerNetworkError    = 0
    ServerUpdateComplete  = 1
    ServerInProgress      = 2
    ServerLatestFiles     = 3
    ServerVersionComplete = 4

    # Version Error states
    VersionNotFound     = {'Not Found' : '404'}
    VersionNetworkError = {'Network'   : 'Error'}

    # Board States
    BoardMango = 'Mango'
    BoardUno   = 'Uno'
    BoardNano  = 'Nano'
    BoardMega  = 'Mega'

    # Class constructor
    def __init__(self):
        super().__init__()
        
        # Available Hex Files
        self.mangoFiles=[]
        self.unoFiles=[]
        self.megaFiles=[]
        self.nanoFiles=[]
        # Thread Variables
        self.getUpdate = False
        self.threadActive = False
        # Start thread to check for new versions  
        self.start()

        # Reading Version Txt File
        with open(PathManager.VersionFilePath, 'r') as f:
          self.version=f.readline()

        # Read all hex files
        self.unoFiles.extend(os.listdir(PathManager.UnoFilesPath))
        self.megaFiles.extend(os.listdir(PathManager.MegaFilesPath))
        self.mangoFiles.extend(os.listdir(PathManager.MangoFilesPath))
        self.nanoFiles.extend(os.listdir(PathManager.NanoFilesPath))

    # Get Internet Response
    def isInternetConnected(self) -> bool:
        try:
            response = requests.get("https://www.google.com", timeout=5)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return True
        except requests.RequestException:
            return False

    # Init Function
    def init(self) -> bool:
        try:
            # Configure Firebase
            firebase = pyrebase.initialize_app(FirebaseCredentials.FirebaseConfigs)
            # Authentication
            auth = firebase.auth() 
            user = auth.sign_in_with_email_and_password(FirebaseCredentials.Email, FirebaseCredentials.Password)
            self.token = user['idToken']
            # Initialize database and storage
            self.database = firebase.database()
            self.storage = firebase.storage()
            # Successful connection
            return True
        # Error connecting to server
        except:
            return False
    
    # Main Thread => Emits update status, update size and version status
    def run(self):  
        if not self.getUpdate:
            self.VersionStatus.emit(self.getNextVersion())
        else:
            downloadFlag = False
            updateState = self.ServerInProgress
            self.threadActive = True
            # Attempt to download
            while (updateState==self.ServerInProgress or updateState==self.ServerVersionComplete) and self.threadActive:
                try:
                    # Get Next Version
                    update = self.getNextVersion()

                    if update == self.VersionNotFound:
                        if downloadFlag:
                            updateState=self.ServerUpdateComplete
                            downloadFlag=False
                        else:
                            updateState=self.ServerLatestFiles
                    elif update == self.VersionNetworkError:
                        updateState=self.ServerNetworkError
                    else:
                        # Getting Update Size
                        self.UpdateSize.emit(update['Size'])
                        update.pop('Size')
                        # Iterating Over Files
                        for board, concatenatedFiles in update.items():
                            # Set Download Flag
                            downloadFlag=True
                            # Getting Current Path and Board Path
                            currentPath = os.getcwd()
                            boardPath = "Hex_Files/"+board

                            # Change directory to download path
                            os.chdir(PathManager.HexFilesEntry+boardPath)
                            # Get existing board files
                            existingFiles = self.getFiles(board)

                            # Generate files list
                            files = concatenatedFiles.split(';;')
                            # Iterate on files
                            for file in files:
                                if file != '':  # Ignore empty files
                                    # Get hex file name and download
                                    mappedFile = PathManager.getHexFile(file)
                                    self.storage.child(f'{self.nextVersionKey}/{board}/{mappedFile}').download(boardPath, mappedFile ,self.token)
                                    self.UpdateStatus.emit(self.ServerInProgress)
                                    # Append to exisitng files
                                    if file not in existingFiles:
                                        existingFiles.append(mappedFile)
                            
                            # Revert to original path
                            os.chdir(currentPath)

                        # Writing New Version
                        self.version=self.nextVersionKey
                        with open(PathManager.VersionFilePath, 'w') as f:
                            f.write(self.version)
                    
                        # Download Complete
                        updateState=self.ServerVersionComplete 

                # Download Failure
                except Exception as e:
                    print(f'Error: {e}')
                    os.chdir(currentPath)
                    updateState = self.ServerNetworkError

                # Emit state
                self.UpdateStatus.emit(updateState)
            # Exit thread
            self.threadActive = False

    # Get details of the next version
    def getNextVersion(self) -> dict:
        if self.isInternetConnected():
        # Initialize Firebase
            if self.init():
                # Get next version number
                versions = list(self.database.get(self.token).val().keys())
                versions = [float(version.replace('_', '.')[1:]) for version in versions]
                versionNumber = float(self.version[1:].replace('_','.'))

                # Return version number if available
                for version in versions:
                    if version > versionNumber:
                        version = str(version).replace('.','_')
                        self.nextVersionKey = f'v{version}'
                        return self.database.child(self.nextVersionKey).get(self.token).val()
                # No verison found
                return self.VersionNotFound
        # Error connecting to server
        return self.VersionNetworkError

    # Check updates
    def checkUpdates(self):
        self.getUpdate = True
        self.start()

    # Terminate thread
    def terminate(self):
        self.threadActive = False
        super().terminate()

    # Get arduino files
    def getFiles(self, arduino:str) -> list:
        if arduino==self.BoardMango:
            return self.mangoFiles
        elif arduino==self.BoardMega:
            return self.megaFiles
        elif arduino==self.BoardNano:
            return self.nanoFiles
        elif arduino==self.BoardUno:
            return self.unoFiles
        else:
            return list()
