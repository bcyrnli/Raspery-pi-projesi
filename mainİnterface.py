import os,sys,shutil
from PyQt5.QtWidgets import QScrollArea,qApp,QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap
mainPc="C:/Users/furka/Desktop/Main Files"
raspEPc="C:/Users/furka/Desktop/E"
raspFPc="C:/Users/furka/Desktop/F"
raspGPc="C:/Users/furka/Desktop/G"
raspHPc="C:/Users/furka/Desktop/H"
copyTest="C:/Users/furka/Desktop/CopyTest"
class MainWin(QScrollArea):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#486581")
        self.init_ui()
    def init_ui(self):
        self.mainPcBut=QPushButton("Ana bilgisayar Dosyaları")
        self.mainPcBut.setStyleSheet("background-color:#bcccdc")
        self.mainPcBut.setShortcut("Return")
        self.raspEfiles=QPushButton("E Dosyaları")
        self.raspEfiles.setStyleSheet("background-color:#bcccdc")
        self.raspFfiles=QPushButton("F dosyaları")
        self.raspFfiles.setStyleSheet("background-color:#bcccdc")
        self.raspGFiles=QPushButton("G dosyaları")
        self.raspGFiles.setStyleSheet("background-color:#bcccdc")
        self.raspHfiles=QPushButton("H Dosyaları")
        self.raspHfiles.setStyleSheet("background-color:#bcccdc")
        self.refresh=QPushButton("Yenile")
        self.refresh.setStyleSheet("background-color:#bcccdc")
        self.caseBut=QPushButton("")
        self.shutdown=QPushButton("")
        self.shutdown.setShortcut("Ctrl+Q")
        self.shutdown.setStyleSheet("border:none;")
        self.caseBut.setStyleSheet("border:none;")
        self.copyPix=QPixmap("copy.png")
        self.delPix=QPixmap("trash.png")
        self.closePix=QPixmap("close.png")
        self.mainfile=0
        self.raspE=0
        self.raspF=0
        self.raspG=0
        self.raspH=0
        self.mainHbox=QHBoxLayout()
        self.mainVbox=QVBoxLayout()
        self.filesBox=QVBoxLayout()
        self.mainVbox.addWidget(self.caseBut)
        self.mainVbox.addWidget(self.mainPcBut)
        self.mainVbox.addWidget(self.raspEfiles)
        self.mainVbox.addWidget(self.raspFfiles)
        self.mainVbox.addWidget(self.raspGFiles)
        self.mainVbox.addWidget(self.raspHfiles)
        self.mainVbox.addWidget(self.refresh)
        self.mainVbox.addStretch()
        self.mainVbox.addWidget(self.shutdown)
        self.mainHbox.addLayout(self.mainVbox)
        self.mainHbox.addLayout(self.filesBox)
        widget=QWidget()
        layout=QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignTop)
        layout.addLayout(self.mainHbox)
        self.setWidget(widget)
        self.setWidgetResizable(True)
        self.setLayout(self.mainHbox)
        self.mainPcBut.clicked.connect(self.mainFilesBut)
        self.raspEfiles.clicked.connect(self.raspEBut)
        self.raspFfiles.clicked.connect(self.raspFBut)
        self.raspGFiles.clicked.connect(self.raspGBut)
        self.raspHfiles.clicked.connect(self.raspHBut)
        self.shutdown.clicked.connect(self.shutDown)
        self.refresh.clicked.connect(self.mainRef)
        self.mainFilesBut()
        self.raspEBut()
        self.raspFBut()
        self.raspGBut()
        self.raspHBut()
        self.show()
    def mainFilesBut(self):
        os.chdir(mainPc)
        mainfiles=os.listdir()
        if len(mainfiles)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:
            self.mainHeaderBut=QPushButton("Ana Bilgisayar Dosyaları")
            self.mainHeaderBut.setStyleSheet("background:#87cefa;"
                                            "font-weight: bold;"
                                        "border-radius:5px;"
                                        "font-family:bold;"
                                        "font-size:24px;")
            self.mainAllCopy = QPushButton("  ")
            self.mainAllCopy.setIcon(QIcon(self.copyPix))
            self.mainAllCopy.setFixedWidth(50)
            self.mainAllCopy.setFixedHeight(25)
            self.mainAllCopy.setIconSize(QSize(50, 35))
            self.mainAllCopy.setStyleSheet("border:none;")
            self.vboxMain=QVBoxLayout()
            self.hboxMain=QHBoxLayout()
            self.hboxMain.addWidget(self.mainHeaderBut)
            self.hboxMain.addWidget(self.mainAllCopy)
            self.vboxMain.addLayout(self.hboxMain)
            for i in mainfiles:
                self.objName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("background:#bcccdc;"
                                         "font-size:20px;"
                                         "margin-left:20px;"
                                         "border-radius:2px;"
                                         "padding-left:10px;"
                                         "padding-right:10px;"
                                         )
                self.mainCopBut=QPushButton("")
                self.mainCopBut.setIcon(QIcon(self.copyPix))
                self.mainCopBut.setFixedWidth(50)
                self.mainCopBut.setFixedHeight(25)
                self.mainCopBut.setIconSize(QSize(50, 35))
                self.mainCopBut.setStyleSheet("border:none;background:#87cefa;"
                                          "border-radius:2px;")
                self.mainCopBut.resize(50, 50)
                self.mainCopBut.setObjectName(self.objName)


                self.mainDelBut = QPushButton("")
                self.mainDelBut.setIcon(QIcon(self.delPix))
                self.mainDelBut.setFixedWidth(50)
                self.mainDelBut.setFixedHeight(25)
                self.mainDelBut.setIconSize(QSize(50, 25))
                self.mainDelBut.setStyleSheet("border:none;background:#87cefa;")
                self.mainDelBut.resize(50, 50)
                self.mainDelBut.setObjectName(self.objName)


                self.filesHbox=QHBoxLayout()
                self.filesHbox.addWidget(self.mainCopBut)
                self.filesHbox.addWidget(self.mainDelBut)
                self.filesHbox.addWidget(self.i)
                self.vboxMain.addLayout(self.filesHbox)
                self.filesBox.addLayout(self.vboxMain)
                self.i.clicked.connect(self.mainClck)
                self.mainCopBut.clicked.connect(self.mainCopy)
                self.mainDelBut.clicked.connect(self.mainDel)
                self.mainfile+=1
            self.mainPcBut.setEnabled(False)
    def mainClck(self):
        os.chdir(mainPc)
        os.startfile(self.sender().text())
    def mainCopy(self):
        os.chdir(mainPc)
        if os.path.isdir(self.sender().objectName()):
            shutil.move(self.sender().objectName(), raspEPc)
            if os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), raspEPc)
        elif os.path.isfile(self.sender().objectName()):
            shutil.copy(self.sender().objectName(), raspEPc)
        else:
            shutil.copy(self.sender().objectName(), raspEPc)
        self.caseBut.setText("Kopyalama İşlemi\nbaşarılı")
        self.caseBut.setStyleSheet("background-color:#c8f902")
    def mainDel(self):
        os.chdir(mainPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def mainClear(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.mainfile
        for k in range(a):
            clearLayout(self.vboxMain.itemAt(k + 1))
        clearLayout(self.hboxMain)
        clearLayout(self.vboxMain)

        self.mainfile = 0

    def raspEBut(self):
        os.chdir(raspEPc)
        filesE=os.listdir()
        if len(filesE)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:
            self.headerEBut=QPushButton("E Dosyaları")
            self.headerEBut.setStyleSheet("background:#002b83;"
                                        "font-weight: bold;"
                                        "border-radius:5px;"
                                        "font-family:bold;"
                                        "font-size:24px;")
            self.butEClear = QPushButton("")
            self.butEClear.setShortcut("Alt+E")
            self.butEClear.setIcon(QIcon(self.closePix))
            self.butEClear.setFixedWidth(50)
            self.butEClear.setFixedHeight(25)
            self.butEClear.setIconSize(QSize(50, 30))
            self.butEClear.setStyleSheet("border:none;")

            self.allECopy = QPushButton("  ")
            self.allECopy.setIcon(QIcon(self.copyPix))
            self.allECopy.setFixedWidth(50)
            self.allECopy.setFixedHeight(25)
            self.allECopy.setIconSize(QSize(50, 35))
            self.allECopy.setStyleSheet("border:none;")

            self.butEClear.clicked.connect(self.clearEBut)
            self.allECopy.clicked.connect(self.allCopyEBut)
            self.vboxE=QVBoxLayout()
            self.hboxE=QHBoxLayout()
            self.hboxE.addWidget(self.headerEBut)
            self.hboxE.addWidget(self.allECopy)
            self.hboxE.addWidget(self.butEClear)
            self.vboxE.addLayout(self.hboxE)
            for i in filesE:
                self.objEName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("background:#bcccdc;"
                                         "font-size:20px;"
                                         "margin-left:20px;"  
                                         "border-radius:2px;"      
                                         "padding-left:10px;"
                                         "padding-right:10px;"
                                         "width:500px;")
                self.copyEBut=QPushButton("")
                self.copyEBut.setIcon(QIcon(self.copyPix))
                self.copyEBut.setFixedWidth(50)
                self.copyEBut.setFixedHeight(25)
                self.copyEBut.setIconSize(QSize(50, 35))
                self.copyEBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")

                self.copyEBut.setObjectName(self.objEName)
                self.delEBut=QPushButton("")
                self.delEBut.setIcon(QIcon(self.delPix))
                self.delEBut.setFixedWidth(50)
                self.delEBut.setFixedHeight(25)
                self.delEBut.setIconSize(QSize(50, 25))
                self.delEBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")
                self.delEBut.setObjectName(self.objEName)
                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyEBut)
                self.filesHBox.addWidget(self.delEBut)
                self.filesHBox.addWidget(self.i)
                self.vboxE.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxE)

                self.i.clicked.connect(self.fileEBut)
                self.copyEBut.clicked.connect(self.copyEClck)
                self.delEBut.clicked.connect(self.delEClck)
                self.raspE+=1
            self.raspEfiles.setEnabled(False)
    def fileEBut(self):
        os.chdir(raspEPc)
        os.startfile(self.sender().text())
    def copyEClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseECopy=0
        for i in mainfiles:
            if i==self.sender().objectName():
                self.caseECopy+=1
                break
        if  self.caseECopy>=1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspEPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delEClck(self):
        os.chdir(raspEPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearEBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspE
        for k in range(a):
            clearLayout(self.vboxE.itemAt(k + 1))
        clearLayout(self.hboxE)
        clearLayout(self.vboxE)
        self.raspEfiles.setEnabled(True)
        self.raspE=0
    def allCopyEBut(self):
        os.chdir(raspEPc)
        filesE=os.listdir()
        for i in filesE:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")


    def raspFBut(self):
        os.chdir(raspFPc)
        filesF=os.listdir()
        self.headerFBut = QPushButton("F Dosyaları")
        self.headerFBut.setStyleSheet("background:#002b83;"
                                      "font-weight: bold;"
                                      "border-radius:5px;"
                                      "font-family:bold;"
                                      "font-size:24px;")

        self.butFClear = QPushButton("")
        self.butFClear.setShortcut("Alt+F")
        self.butFClear.setIcon(QIcon(self.closePix))
        self.butFClear.setFixedWidth(50)
        self.butFClear.setFixedHeight(25)
        self.butFClear.setIconSize(QSize(50, 30))
        self.butFClear.setStyleSheet("border:none;")

        self.allFCopy = QPushButton("  ")
        self.allFCopy.setIcon(QIcon(self.copyPix))
        self.allFCopy.setFixedWidth(50)
        self.allFCopy.setFixedHeight(25)
        self.allFCopy.setIconSize(QSize(50, 35))
        self.allFCopy.setStyleSheet("border:none;")

        self.butFClear.clicked.connect(self.clearFBut)
        self.allFCopy.clicked.connect(self.allCopyFBut)
        self.vboxF = QVBoxLayout()
        self.hboxF = QHBoxLayout()
        self.hboxF.addWidget(self.headerFBut)
        self.hboxF.addWidget(self.allFCopy)
        self.hboxF.addWidget(self.butFClear)
        self.vboxF.addLayout(self.hboxF)
        self.filesBox.addLayout(self.vboxF)
        self.raspFfiles.setEnabled(False)
        if len(filesF)==0:
            self.caseBut.setText("F Klasörü Boş")
            self.caseBut.setStyleSheet("background-color:yellow;font-size:16px;")
        else:

            for i in filesF:
                self.objFName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("background:#bcccdc;"
                                         "font-size:20px;"
                                         "margin-left:20px;"  
                                         "border-radius:2px;"      
                                         "padding-left:10px;"
                                         "padding-right:10px;"
                                         "width:500px;")
                self.copyFBut=QPushButton("")
                self.copyFBut.setIcon(QIcon(self.copyPix))
                self.copyFBut.setFixedWidth(50)
                self.copyFBut.setFixedHeight(25)
                self.copyFBut.setIconSize(QSize(50, 35))
                self.copyFBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")

                self.copyFBut.setObjectName(self.objFName)
                self.delFBut=QPushButton("")
                self.delFBut.setIcon(QIcon(self.delPix))
                self.delFBut.setFixedWidth(50)
                self.delFBut.setFixedHeight(25)
                self.delFBut.setIconSize(QSize(50, 25))
                self.delFBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")
                self.delFBut.setObjectName(self.objFName)

                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyFBut)
                self.filesHBox.addWidget(self.delFBut)
                self.filesHBox.addWidget(self.i)
                self.vboxF.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxF)

                self.i.clicked.connect(self.fileFBut)
                self.copyFBut.clicked.connect(self.copyFClck)
                self.delFBut.clicked.connect(self.delFClck)
                self.raspF+=1
            self.raspFfiles.setEnabled(False)
    def fileFBut(self):
        os.chdir(raspFPc)
        os.startfile(self.sender().text())
    def copyFClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseFCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseFCopy += 1
                break
        if self.caseFCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspFPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delFClck(self):
        os.chdir(raspFPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearFBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspF
        for k in range(a):
            clearLayout(self.vboxF.itemAt(k + 1))
        clearLayout(self.hboxF)
        clearLayout(self.vboxF)
        self.raspFfiles.setEnabled(True)
        self.raspF=0
    def allCopyFBut(self):
        os.chdir(raspFPc)
        filesF=os.listdir()
        for i in filesF:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def raspGBut(self):
        os.chdir(raspGPc)
        filesG=os.listdir()
        self.headerGBut = QPushButton("G Dosyaları")
        self.headerGBut.setStyleSheet("background:#002b83;"
                                      "font-weight: bold;"
                                      "border-radius:5px;"
                                      "font-family:bold;"
                                      "font-size:24px;")
        self.butGClear = QPushButton("")
        self.butGClear.setShortcut("Alt+G")
        self.butGClear.setIcon(QIcon(self.closePix))
        self.butGClear.setFixedWidth(50)
        self.butGClear.setFixedHeight(25)
        self.butGClear.setIconSize(QSize(50, 30))
        self.butGClear.setStyleSheet("border:none;")

        self.allGCopy = QPushButton("  ")
        self.allGCopy.setIcon(QIcon(self.copyPix))
        self.allGCopy.setFixedWidth(50)
        self.allGCopy.setFixedHeight(25)
        self.allGCopy.setIconSize(QSize(50, 35))
        self.allGCopy.setStyleSheet("border:none;")

        self.butGClear.clicked.connect(self.clearGBut)
        self.allGCopy.clicked.connect(self.allCopyGBut)
        self.vboxG = QVBoxLayout()
        self.hboxG = QHBoxLayout()
        self.hboxG.addWidget(self.headerGBut)
        self.hboxG.addWidget(self.allGCopy)
        self.hboxG.addWidget(self.butGClear)
        self.vboxG.addLayout(self.hboxG)
        self.filesBox.addLayout(self.vboxG)
        if len(filesG)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:

            for i in filesG:
                self.objGName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("background:#bcccdc;"
                                         "font-size:20px;"
                                         "margin-left:20px;"  
                                         "border-radius:2px;"      
                                         "padding-left:10px;"
                                         "padding-right:10px;"
                                         "width:500px;")
                self.copyGBut=QPushButton("")
                self.copyGBut.setIcon(QIcon(self.copyPix))
                self.copyGBut.setFixedWidth(50)
                self.copyGBut.setFixedHeight(25)
                self.copyGBut.setIconSize(QSize(50, 35))
                self.copyGBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")
                self.copyGBut.setObjectName(self.objGName)

                self.delGBut=QPushButton("")
                self.delGBut.setIcon(QIcon(self.delPix))
                self.delGBut.setFixedWidth(50)
                self.delGBut.setFixedHeight(25)
                self.delGBut.setIconSize(QSize(50, 25))
                self.delGBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")

                self.delGBut.setObjectName(self.objGName)
                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyGBut)
                self.filesHBox.addWidget(self.delGBut)
                self.filesHBox.addWidget(self.i)
                self.vboxG.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxG)

                self.i.clicked.connect(self.fileGBut)
                self.copyGBut.clicked.connect(self.copyGClck)
                self.delGBut.clicked.connect(self.delGClck)
                self.raspG+=1
            self.raspGFiles.setEnabled(False)
    def fileGBut(self):
        os.chdir(raspFPc)
        os.startfile(self.sender().text())
    def copyGClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseGCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseGCopy += 1
                break
        if self.caseGCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspGPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delGClck(self):
        os.chdir(raspGPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearGBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspG
        for k in range(a):
            clearLayout(self.vboxG.itemAt(k + 1))
        clearLayout(self.hboxG)
        clearLayout(self.vboxG)
        self.raspGFiles.setEnabled(True)
        self.raspG=0
    def allCopyGBut(self):
        os.chdir(raspGPc)
        filesG=os.listdir()
        for i in filesG:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def raspHBut(self):
        os.chdir(raspHPc)
        filesH=os.listdir()
        self.headerHBut = QPushButton("H Dosyaları")
        self.headerHBut.setStyleSheet("background:#002b83;"
                                      "font-weight: bold;"
                                      "border-radius:5px;"
                                      "font-family:bold;"
                                      "font-size:24px;")
        self.butHClear = QPushButton("")
        self.butHClear.setShortcut("Alt+H")
        self.butHClear.setIcon(QIcon(self.closePix))
        self.butHClear.setFixedWidth(50)
        self.butHClear.setFixedHeight(25)
        self.butHClear.setIconSize(QSize(50, 30))
        self.butHClear.setStyleSheet("border:none;")

        self.allHCopy = QPushButton("  ")
        self.allHCopy.setIcon(QIcon(self.copyPix))
        self.allHCopy.setFixedWidth(50)
        self.allHCopy.setFixedHeight(25)
        self.allHCopy.setIconSize(QSize(50, 35))
        self.allHCopy.setStyleSheet("border:none;")

        self.butHClear.clicked.connect(self.clearHBut)
        self.allHCopy.clicked.connect(self.allCopyHBut)
        self.vboxH = QVBoxLayout()
        self.hboxH = QHBoxLayout()
        self.hboxH.addWidget(self.headerHBut)
        self.hboxH.addWidget(self.allHCopy)
        self.hboxH.addWidget(self.butHClear)
        self.vboxH.addLayout(self.hboxH)
        self.filesBox.addLayout(self.vboxH)
        if len(filesH)==0:
            self.caseBut.setText("Klasör Boş")
            self.caseBut.setStyleSheet("background-color:green;font-size:16px;")
        else:

            for i in filesH:
                self.objHName=i
                self.i=QPushButton(i)
                self.i.setStyleSheet("background:#bcccdc;"
                                         "font-size:20px;"
                                         "margin-left:20px;"  
                                         "border-radius:2px;"      
                                         "padding-left:10px;"
                                         "padding-right:10px;"
                                         "width:500px;")
                self.copyHBut=QPushButton("")
                self.copyHBut.setIcon(QIcon(self.copyPix))
                self.copyHBut.setFixedWidth(50)
                self.copyHBut.setFixedHeight(25)
                self.copyHBut.setIconSize(QSize(50, 35))
                self.copyHBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")
                self.copyHBut.setObjectName(self.objHName)

                self.delHBut=QPushButton("")
                self.delHBut.setIcon(QIcon(self.delPix))
                self.delHBut.setFixedWidth(50)
                self.delHBut.setFixedHeight(25)
                self.delHBut.setIconSize(QSize(50, 25))
                self.delHBut.setStyleSheet("border:none;background:#002b83;"
                                          "border-radius:2px;")
                self.delHBut.setObjectName(self.objGName)

                self.filesHBox=QHBoxLayout()
                self.filesHBox.addWidget(self.copyHBut)
                self.filesHBox.addWidget(self.delHBut)
                self.filesHBox.addWidget(self.i)
                self.vboxH.addLayout(self.filesHBox)
                self.filesBox.addLayout(self.vboxH)

                self.i.clicked.connect(self.fileHBut)
                self.copyHBut.clicked.connect(self.copyHClck)
                self.delHBut.clicked.connect(self.delHClck)
                self.raspH+=1
            self.raspHfiles.setEnabled(False)
    def fileHBut(self):
        os.chdir(raspHPc)
        os.startfile(self.sender().text())
    def copyHClck(self):
        os.chdir(mainPc)
        mainfiles = os.listdir()
        self.caseHCopy = 0
        for i in mainfiles:
            if i == self.sender().objectName():
                self.caseHCopy += 1
                break
        if self.caseHCopy >= 1:
            self.caseBut.setText("Bu İsimde Bir\nDosya Zaten Var")
            self.caseBut.setStyleSheet("background-color:#c8f902")
        else:
            os.chdir(raspHPc)
            if os.path.isdir(self.sender().objectName()):
                shutil.move(self.sender().objectName(), mainPc)
                if os.path.isfile(self.sender().objectName()):
                    shutil.copy(self.sender().objectName(), mainPc)
            elif os.path.isfile(self.sender().objectName()):
                shutil.copy(self.sender().objectName(), mainPc)
            else:
                shutil.copy(self.sender().objectName(), mainPc)
            self.mainCopy()
    def delHClck(self):
        os.chdir(raspHPc)
        if os.path.isdir(self.sender().objectName()):
            os.rmdir(self.sender().objectName())
        elif os.path.isfile(self.sender().objectName()):
            os.remove(self.sender().objectName())
        else:
            os.remove(self.sender().objectName())
        self.mainRef()
    def clearHBut(self):
        def clearLayout(layout):
            while layout.count() > 0:
                item = layout.takeAt(0)
                if not item:
                    continue
                w = item.widget()
                if w:
                    w.deleteLater()

        a = self.raspH
        for k in range(a):
            clearLayout(self.vboxH.itemAt(k + 1))
        clearLayout(self.hboxH)
        clearLayout(self.vboxH)
        self.raspHfiles.setEnabled(True)
        self.raspH=0
    def allCopyHBut(self):
        os.chdir(raspHPc)
        filesH=os.listdir()
        for i in filesH:
            if os.path.isdir(i):
                shutil.move(i, copyTest)
                if os.path.isfile(i):
                    shutil.copy(i, copyTest)
            elif os.path.isfile(i):
                shutil.copy(i, copyTest)
            else:
                shutil.copy(i, copyTest)
        self.caseBut.setText("Bütün Dosyalar\nKopyalandı")
        self.caseBut.setStyleSheet("background-color:green;border:none;font-size:16px")

    def shutDown(self):
        qApp.quit()
    def mainRef(self):
        self.mainClear()
        self.clearEBut()
        self.clearFBut()
        self.clearGBut()
        self.clearHBut()
        self.caseBut.setText("Yenileniyor...")
        self.caseBut.setStyleSheet("background-color:#c8f902")
        self.mainFilesBut()
        self.raspEBut()
        self.raspFBut()
        self.raspGBut()
        self.raspHBut()
        self.caseBut.setText("Yenilendi")
        self.caseBut.setStyleSheet("background-color:#c8f902")
    def mainCopy(self):
        self.copiedHbox = QHBoxLayout()
        self.copiedObjName = self.sender().objectName()
        self.copiedFile = QPushButton(self.sender().objectName())
        self.copiedFile.setStyleSheet("background:#bcccdc;"
                                      "font-size:20px;"
                                      "margin-left:20px;"
                                      "border-radius:2px;"
                                      "padding-left:10px;"
                                      "padding-right:10px;"
                                      "width:500px;")

        self.copiedCopBut = QPushButton("")
        self.copiedCopBut.setIcon(QIcon(self.copyPix))
        self.copiedCopBut.setFixedWidth(50)
        self.copiedCopBut.setFixedHeight(25)
        self.copiedCopBut.setIconSize(QSize(50, 25))
        self.copiedCopBut.setStyleSheet("border:none;background:#87cefa;"
                                        "border-radius:2px;")
        self.copiedCopBut.resize(50, 50)
        self.copiedCopBut.setObjectName(self.copiedObjName)

        self.copiedDelBut = QPushButton("")
        self.copiedDelBut.setIcon(QIcon(self.delPix))
        self.copiedDelBut.setFixedWidth(50)
        self.copiedDelBut.setFixedHeight(25)
        self.copiedDelBut.setIconSize(QSize(50, 25))
        self.copiedDelBut.setStyleSheet("border:none;background:#87cefa;")
        self.copiedDelBut.resize(50, 50)
        self.copiedDelBut.setObjectName(self.copiedObjName)

        self.copiedHbox.addWidget(self.copiedCopBut)
        self.copiedHbox.addWidget(self.copiedDelBut)
        self.copiedHbox.addWidget(self.copiedFile)
        self.vboxMain.addLayout(self.copiedHbox)
        self.copiedFile.clicked.connect(self.mainClck)
        self.copiedCopBut.clicked.connect(self.mainCopy)
        self.copiedDelBut.clicked.connect(self.mainDel)
app=QApplication(sys.argv)
win=MainWin()
win.setWindowTitle("Main İnterface")
win.setGeometry(800,200,800,800)
sys.exit(app.exec_())