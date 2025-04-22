##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# Config Files #

class PathManager:
    # Script Paths
    HexFilesEntry       = "./"
    UnoFilesPath        = "./Hex_Files/Uno/"
    MegaFilesPath       = "./Hex_Files/Mega/"
    NanoFilesPath       = "./Hex_Files/Nano/"
    MangoFilesPath      = "./Hex_Files/Mango/"
    DownloadGifPath     = ":/GIFs/download.gif"
    NoWifiGifPath       = ":/GIFs/no_wifi.gif"
    WifiGifPath         = ":/GIFs/wifi.gif"
    RndGifPath          = ":/GIFs/rnd.gif" 
    LoadingGifPath      = ":/GIFs/loading.gif"
    LoadingPngPath      = ":/Labels/loading.png"
    GreenPngPath        = ":/Labels/green.png"
    RedPngPath          = ":/Labels/red.png" 
    UpdatePngPath       = ":/Icons/update.png"
    NotificationPngPath = ":/Icons/notification.png"
    VersionFilePath     = "./Utils/version.md"
    AvrDudePath         = './Utils/avrdude -C ./Utils/avrdude.conf'

    # Hex Files Map
    def getHexFile(project_name):
        hex_files_map = {
            'blink'   : 'Blink.hex',
            'erase'   : 'eeprom_clear.hex'
        }
        return hex_files_map.get(project_name.lower(), 'Blink.hex')
    