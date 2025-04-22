##########################################################################################
####################### Project: Arduino Upload GUI                #######################
####################### Version: 1.4                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 21/10/2024                          #######################
##########################################################################################

# UI File #

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QProgressBar, QPushButton, QRadioButton, QScrollArea, QSizePolicy, QToolBox, QVBoxLayout, QWidget
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont, QIcon, QPixmap
import resources

class ArduinoUI(object):
    def setupUi(self, Arduino):
        if not Arduino.objectName():
            Arduino.setObjectName(u"Arduino")
        Arduino.resize(750, 600)
        Arduino.setMinimumSize(QSize(750, 600))
        Arduino.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        Arduino.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Icons/orange.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Arduino.setWindowIcon(icon)
        Arduino.setStyleSheet(u"QWidget#Arduino{\n"
"background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: rgba(255,255,255,100);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/Icons/unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/Icons/hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Icons/checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    imag"
                        "e: url(:/Icons/checked_hover.png);\n"
"}\n"
"\n"
"QMessageBox {\n"
" background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"  width: 400px; \n"
"  height: 400px;\n"
"}\n"
"QMessageBox QLabel {\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QMessageBox QPushButton {\n"
"   	background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"  	font-size: 14px;\n"
"  	min-height: 15px; \n"
"  	min-width: 60px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"  background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"   background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}")
        self.verticalLayout = QVBoxLayout(Arduino)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 10, 5, 10)
        self.topFrame = QFrame(Arduino)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setStyleSheet(u"")
        self.topFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.animationFrame = QFrame(self.topFrame)
        self.animationFrame.setObjectName(u"animationFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.animationFrame.sizePolicy().hasHeightForWidth())
        self.animationFrame.setSizePolicy(sizePolicy)
        self.animationFrame.setMaximumSize(QSize(16777215, 16777215))
        self.animationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.animationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.animationFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topAnimation = QLabel(self.animationFrame)
        self.topAnimation.setObjectName(u"topAnimation")
        sizePolicy.setHeightForWidth(self.topAnimation.sizePolicy().hasHeightForWidth())
        self.topAnimation.setSizePolicy(sizePolicy)
        self.topAnimation.setMinimumSize(QSize(0, 60))
        self.topAnimation.setMaximumSize(QSize(60, 60))
        self.topAnimation.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.topAnimation)


        self.horizontalLayout_2.addWidget(self.animationFrame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.topFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.middleFrame = QFrame(Arduino)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy1)
        self.middleFrame.setStyleSheet(u"")
        self.middleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.middleFrame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, -1, 20, 10)
        self.projectFrame = QFrame(self.middleFrame)
        self.projectFrame.setObjectName(u"projectFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projectFrame.sizePolicy().hasHeightForWidth())
        self.projectFrame.setSizePolicy(sizePolicy2)
        self.projectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.projectFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.projectSelector = QToolBox(self.projectFrame)
        self.projectSelector.setObjectName(u"projectSelector")
        font1 = QFont()
        font1.setPointSize(14)
        self.projectSelector.setFont(font1)
        self.projectSelector.setStyleSheet(u"QToolBox::tab {\n"
"    background: transparent; \n"
"    color: white;       \n"
"    padding: 0px 5px; \n"
"	color:rgb(200, 135, 100);     \n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"	color: rgb(255, 120, 20);   \n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"   color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox {\n"
"    background:rgba(55, 55, 55, 120);\n"
"    padding: 10px;  \n"
"}\n"
"\n"
"QToolBox QWidget {\n"
"   background-color:transparent;\n"
"    border: none; \n"
"}\n"
"\n"
"QToolBox QPushButton {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QToolBox QPushButton:disabled{\n"
"color: rgba(255,255,255,100);\n"
"}\n"
"")
        self.projectsWidget = QWidget()
        self.projectsWidget.setObjectName(u"projectsWidget")
        self.projectsWidget.setGeometry(QRect(0, 0, 486, 289))
        self.verticalLayout_16 = QVBoxLayout(self.projectsWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.projectsFrame = QFrame(self.projectsWidget)
        self.projectsFrame.setObjectName(u"projectsFrame")
        self.projectsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.projectsFrame)
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 0, 5, 0)
        self.projectSubFrame1 = QFrame(self.projectsFrame)
        self.projectSubFrame1.setObjectName(u"projectSubFrame1")
        self.projectSubFrame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectSubFrame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.projectSubFrame1)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.projectButton1 = QPushButton(self.projectSubFrame1)
        self.projectButton1.setObjectName(u"projectButton1")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.projectButton1.setFont(font2)
        self.projectButton1.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/car.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectButton1.setIcon(icon1)
        self.projectButton1.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.projectButton1)

        self.projectButton2 = QPushButton(self.projectSubFrame1)
        self.projectButton2.setObjectName(u"projectButton2")
        self.projectButton2.setFont(font2)
        self.projectButton2.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/robot-arm.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectButton2.setIcon(icon2)
        self.projectButton2.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.projectButton2)

        self.projectButton3 = QPushButton(self.projectSubFrame1)
        self.projectButton3.setObjectName(u"projectButton3")
        self.projectButton3.setFont(font2)
        self.projectButton3.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/head.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectButton3.setIcon(icon3)
        self.projectButton3.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.projectButton3)


        self.verticalLayout_19.addWidget(self.projectSubFrame1, 0, Qt.AlignmentFlag.AlignTop)

        self.projectSubFrame2 = QFrame(self.projectsFrame)
        self.projectSubFrame2.setObjectName(u"projectSubFrame2")
        self.projectSubFrame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectSubFrame2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.projectSubFrame2)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.projectButton4 = QPushButton(self.projectSubFrame2)
        self.projectButton4.setObjectName(u"projectButton4")
        self.projectButton4.setFont(font2)
        self.projectButton4.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/bot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectButton4.setIcon(icon4)
        self.projectButton4.setIconSize(QSize(30, 30))

        self.horizontalLayout_15.addWidget(self.projectButton4)

        self.projectButton5 = QPushButton(self.projectSubFrame2)
        self.projectButton5.setObjectName(u"projectButton5")
        self.projectButton5.setFont(font2)
        self.projectButton5.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/ninja.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectButton5.setIcon(icon5)
        self.projectButton5.setIconSize(QSize(30, 30))

        self.horizontalLayout_15.addWidget(self.projectButton5)


        self.verticalLayout_19.addWidget(self.projectSubFrame2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_16.addWidget(self.projectsFrame)

        icon6 = QIcon()
        icon6.addFile(u":/Icons/work.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectSelector.addItem(self.projectsWidget, icon6, u"Projects")
        self.testWidget = QWidget()
        self.testWidget.setObjectName(u"testWidget")
        self.testWidget.setGeometry(QRect(0, 0, 486, 289))
        self.verticalLayout_12 = QVBoxLayout(self.testWidget)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 0, 5, 0)
        self.outputFrame = QFrame(self.testWidget)
        self.outputFrame.setObjectName(u"outputFrame")
        self.outputFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.outputFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.outputFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.testFrame = QFrame(self.outputFrame)
        self.testFrame.setObjectName(u"testFrame")
        self.testFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.testFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.testFrame)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.eraseButton = QPushButton(self.testFrame)
        self.eraseButton.setObjectName(u"eraseButton")
        self.eraseButton.setFont(font2)
        self.eraseButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(90, 225, 115, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(90, 225, 115, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Icons/chip.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eraseButton.setIcon(icon7)
        self.eraseButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.eraseButton, 0, Qt.AlignmentFlag.AlignTop)

        self.blinkButton = QPushButton(self.testFrame)
        self.blinkButton.setObjectName(u"blinkButton")
        self.blinkButton.setFont(font2)
        self.blinkButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(90, 225, 115, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(90, 225, 115, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/blink.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.blinkButton.setIcon(icon8)
        self.blinkButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.blinkButton, 0, Qt.AlignmentFlag.AlignTop)

        self.hexButton = QPushButton(self.testFrame)
        self.hexButton.setObjectName(u"hexButton")
        self.hexButton.setFont(font2)
        self.hexButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(90, 225, 115, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(90, 225, 115, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/code.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hexButton.setIcon(icon9)
        self.hexButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.hexButton, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_14.addWidget(self.testFrame)

        self.scrollArea = QScrollArea(self.outputFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QAbstractScrollArea\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color:rgb(30, 30, 30);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background: rgba(200, 200, 200, 255);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"   background: rgba(255, 144, 0, 255);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background: rgba(255, 80, 0, 255);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image:  url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image :url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
" "
                        "   subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    background-color:rgb(30, 30, 30);\n"
"    height: 14px; \n"
"    margin: 0 15px 0 15px;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollB"
                        "ar::handle:horizontal\n"
"{\n"
"    background: rgba(200, 200, 200, 255);\n"
"    min-width: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover\n"
"{\n"
"   background: rgba(255, 144, 0, 255);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed\n"
"{\n"
"   background: rgba(255, 80, 0, 255);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Icons/left_arrow.png); \n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: left; \n"
"    subcontrol-origin: margin; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    margin: 0px 3px 0px 3px;\n"
"    border-image: url(:/Icons/right_arrow.png); \n"
"    width: 10px; \n"
"    height: 10px;\n"
"    subcontrol-position: right; \n"
"    subcontrol-origin: margin; \n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover,QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image:  url(:/Icons/left_arrow.png); \n"
"}\n"
"\n"
"QScrollBar::add-line:horiz"
                        "ontal:hover, QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/Icons/right_arrow.png); \n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setGeometry(QRect(0, 0, 476, 245))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaContent)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 10, 0, 0)
        self.outputUpload = QLabel(self.scrollAreaContent)
        self.outputUpload.setObjectName(u"outputUpload")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.outputUpload.sizePolicy().hasHeightForWidth())
        self.outputUpload.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(10)
        self.outputUpload.setFont(font3)
        self.outputUpload.setStyleSheet(u"color: white;\n"
"background-color:rgba(30, 30, 30,200);\n"
"padding:5px;")
        self.outputUpload.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.outputUpload.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.outputUpload)

        self.scrollArea.setWidget(self.scrollAreaContent)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_12.addWidget(self.outputFrame)

        icon10 = QIcon()
        icon10.addFile(u":/Icons/test.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.projectSelector.addItem(self.testWidget, icon10, u"Test Board")

        self.verticalLayout_2.addWidget(self.projectSelector)


        self.horizontalLayout_3.addWidget(self.projectFrame)

        self.selectionFrame = QFrame(self.middleFrame)
        self.selectionFrame.setObjectName(u"selectionFrame")
        self.selectionFrame.setStyleSheet(u"QFrame #selectionFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.selectionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.selectionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.selectionFrame)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 20, 10, 20)
        self.selectFrame = QFrame(self.selectionFrame)
        self.selectFrame.setObjectName(u"selectFrame")
        self.selectFrame.setStyleSheet(u"background-color: rgba(255, 135, 17,100);")
        self.selectFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.selectFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.selectFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.selectBoardLabel = QLabel(self.selectFrame)
        self.selectBoardLabel.setObjectName(u"selectBoardLabel")
        self.selectBoardLabel.setFont(font1)
        self.selectBoardLabel.setStyleSheet(u"background-color:transparent;\n"
"color: white;")
        self.selectBoardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.selectBoardLabel)


        self.verticalLayout_7.addWidget(self.selectFrame)

        self.boardsFrame = QFrame(self.selectionFrame)
        self.boardsFrame.setObjectName(u"boardsFrame")
        self.boardsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.boardsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.boardsFrame)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.mangoRadio = QRadioButton(self.boardsFrame)
        self.mangoRadio.setObjectName(u"mangoRadio")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(False)
        self.mangoRadio.setFont(font4)
        self.mangoRadio.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_6.addWidget(self.mangoRadio)

        self.unoRadio = QRadioButton(self.boardsFrame)
        self.unoRadio.setObjectName(u"unoRadio")
        self.unoRadio.setFont(font4)
        self.unoRadio.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_6.addWidget(self.unoRadio)

        self.nanoRadio = QRadioButton(self.boardsFrame)
        self.nanoRadio.setObjectName(u"nanoRadio")
        self.nanoRadio.setFont(font4)
        self.nanoRadio.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_6.addWidget(self.nanoRadio)

        self.megaRadio = QRadioButton(self.boardsFrame)
        self.megaRadio.setObjectName(u"megaRadio")
        self.megaRadio.setFont(font4)
        self.megaRadio.setStyleSheet(u"color: #FFFFFF;")

        self.verticalLayout_6.addWidget(self.megaRadio)


        self.verticalLayout_7.addWidget(self.boardsFrame)

        self.updateFrame = QFrame(self.selectionFrame)
        self.updateFrame.setObjectName(u"updateFrame")
        self.updateFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.updateFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.updateFrame)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 40, 0, -1)
        self.updateButton = QPushButton(self.updateFrame)
        self.updateButton.setObjectName(u"updateButton")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.updateButton.setFont(font5)
        self.updateButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(255, 30, 30, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color :rgba(255, 30, 30, 150);    \n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/Icons/update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.updateButton.setIcon(icon11)
        self.updateButton.setIconSize(QSize(35, 35))

        self.verticalLayout_4.addWidget(self.updateButton)


        self.verticalLayout_7.addWidget(self.updateFrame)


        self.horizontalLayout_3.addWidget(self.selectionFrame, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.middleFrame)

        self.bottomFrame = QFrame(Arduino)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setStyleSheet(u"")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 10)
        self.progressConnectionFrame = QFrame(self.bottomFrame)
        self.progressConnectionFrame.setObjectName(u"progressConnectionFrame")
        sizePolicy2.setHeightForWidth(self.progressConnectionFrame.sizePolicy().hasHeightForWidth())
        self.progressConnectionFrame.setSizePolicy(sizePolicy2)
        self.progressConnectionFrame.setStyleSheet(u"QFrame #progressConnectionFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.progressConnectionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressConnectionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.progressConnectionFrame)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.connectionFrame = QFrame(self.progressConnectionFrame)
        self.connectionFrame.setObjectName(u"connectionFrame")
        self.connectionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.connectionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.connectionFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.connectionLabel = QLabel(self.connectionFrame)
        self.connectionLabel.setObjectName(u"connectionLabel")
        self.connectionLabel.setMaximumSize(QSize(60, 60))
        self.connectionLabel.setPixmap(QPixmap(u":/Labels/red.png"))
        self.connectionLabel.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.connectionLabel)


        self.horizontalLayout_8.addWidget(self.connectionFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.progressFrame = QFrame(self.progressConnectionFrame)
        self.progressFrame.setObjectName(u"progressFrame")
        sizePolicy2.setHeightForWidth(self.progressFrame.sizePolicy().hasHeightForWidth())
        self.progressFrame.setSizePolicy(sizePolicy2)
        self.progressFrame.setStyleSheet(u"QLabel {\n"
"color: white;\n"
"border-radius:0px;\n"
"padding: 2px;\n"
"border-bottom: 2px solid red;\n"
"}")
        self.progressFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.progressFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.progressFrame)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.portLabel = QLabel(self.progressFrame)
        self.portLabel.setObjectName(u"portLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.portLabel.sizePolicy().hasHeightForWidth())
        self.portLabel.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        self.portLabel.setFont(font6)
        self.portLabel.setStyleSheet(u"")
        self.portLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.portLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.progressBar = QProgressBar(self.progressFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMouseTracking(False)
        self.progressBar.setTabletTracking(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"background-color:transparent;\n"
"border-radius: 7px;\n"
"border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"border-radius: 6px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.1 rgb(200, 200, 200), stop:1 rgb(255, 147, 21));\n"
"}")
        self.progressBar.setValue(100)
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.verticalLayout_9.addWidget(self.progressBar)


        self.horizontalLayout_8.addWidget(self.progressFrame)


        self.horizontalLayout.addWidget(self.progressConnectionFrame)

        self.rndFrame = QFrame(self.bottomFrame)
        self.rndFrame.setObjectName(u"rndFrame")
        self.rndFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rndFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.rndFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bottomAnimationFrame = QFrame(self.rndFrame)
        self.bottomAnimationFrame.setObjectName(u"bottomAnimationFrame")
        self.bottomAnimationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomAnimationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottomAnimationFrame)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bottomAnimation = QLabel(self.bottomAnimationFrame)
        self.bottomAnimation.setObjectName(u"bottomAnimation")
        self.bottomAnimation.setMinimumSize(QSize(0, 60))
        self.bottomAnimation.setMaximumSize(QSize(16777215, 60))
        self.bottomAnimation.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.bottomAnimation, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.bottomAnimationFrame)


        self.horizontalLayout.addWidget(self.rndFrame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.bottomFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(Arduino)

        self.projectSelector.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Arduino)
    # setupUi

    def retranslateUi(self, Arduino):
        Arduino.setWindowTitle(QCoreApplication.translate("Arduino", u"Arduino Uploader", None))
        self.topAnimation.setText("")
        self.projectButton1.setText(QCoreApplication.translate("Arduino", u"Project 1", None))
        self.projectButton2.setText(QCoreApplication.translate("Arduino", u"Project 2", None))
        self.projectButton3.setText(QCoreApplication.translate("Arduino", u"Project 3", None))
        self.projectButton4.setText(QCoreApplication.translate("Arduino", u"Project 4", None))
        self.projectButton5.setText(QCoreApplication.translate("Arduino", u"Project 5", None))
        self.projectSelector.setItemText(self.projectSelector.indexOf(self.projectsWidget), QCoreApplication.translate("Arduino", u"Projects", None))
        self.eraseButton.setText(QCoreApplication.translate("Arduino", u"Clear Memory", None))
        self.blinkButton.setText(QCoreApplication.translate("Arduino", u"Blink Led", None))
        self.hexButton.setText(QCoreApplication.translate("Arduino", u"Custom Code", None))
        self.outputUpload.setText("")
        self.projectSelector.setItemText(self.projectSelector.indexOf(self.testWidget), QCoreApplication.translate("Arduino", u"Test Board", None))
        self.selectBoardLabel.setText(QCoreApplication.translate("Arduino", u"Select Board", None))
        self.mangoRadio.setText(QCoreApplication.translate("Arduino", u"Mango Uno", None))
        self.unoRadio.setText(QCoreApplication.translate("Arduino", u"Uno", None))
        self.nanoRadio.setText(QCoreApplication.translate("Arduino", u"Nano", None))
        self.megaRadio.setText(QCoreApplication.translate("Arduino", u"Mega 2560", None))
        self.updateButton.setText(QCoreApplication.translate("Arduino", u"Update Projects", None))
        self.connectionLabel.setText("")
        self.portLabel.setText(QCoreApplication.translate("Arduino", u"Arduino Not Connected ", None))
        self.bottomAnimation.setText("")
    # retranslateUi

