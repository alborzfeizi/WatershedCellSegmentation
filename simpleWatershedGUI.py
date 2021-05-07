# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QTextEdit
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from skimage import color
from scipy import ndimage
import numpy as np
import imutils
import cv2
import copy

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1130, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.watershedButton = QtWidgets.QPushButton(self.centralwidget)
        self.watershedButton.setGeometry(QtCore.QRect(410, 520, 141, 41))
        self.watershedButton.setObjectName("watershedButton")
        
        self.filepathTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.filepathTextEdit.setGeometry(QtCore.QRect(20, 40, 531, 31))
        self.filepathTextEdit.setObjectName("filepathTextEdit")
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label1.setObjectName("label1")
        
        self.image1Label = QtWidgets.QLabel(self.centralwidget)
        self.image1Label.setGeometry(QtCore.QRect(20, 80, 531, 435))
        self.image1Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image1Label.setAutoFillBackground(False)
        self.image1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image1Label.setText("")
        #self.image1Label.setPixmap(QtGui.QPixmap("D:/A02.2020-08-27-20-07-49/A02_Bottom Slide_R_p01_0_A01f00d0.TIF"))
        self.image1Label.setScaledContents(True)
        self.image1Label.setObjectName("image1Label")
        
        self.min_distanceSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.min_distanceSpinBox.setGeometry(QtCore.QRect(350, 530, 42, 22))
        self.min_distanceSpinBox.setMinimum(1)
        self.min_distanceSpinBox.setProperty("value", 10)
        self.min_distanceSpinBox.setObjectName("min_distanceSpinBox")
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(270, 530, 81, 20))
        self.label2.setObjectName("label2")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(570, 55, 531, 461))
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.image2Label = QtWidgets.QLabel(self.tab1)
        self.image2Label.setGeometry(QtCore.QRect(0, 0, 531, 435))
        self.image2Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image2Label.setAutoFillBackground(False)
        self.image2Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image2Label.setText("")
        #self.image2Label.setPixmap(QtGui.QPixmap("D:/A02.2020-08-27-20-07-49/A02_Bottom Slide_R_p01_0_A01f00d0.TIF"))
        self.image2Label.setScaledContents(True)
        self.image2Label.setObjectName("image2Label")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.image3Label = QtWidgets.QLabel(self.tab2)
        self.image3Label.setGeometry(QtCore.QRect(0, 0, 531, 435))
        self.image3Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image3Label.setAutoFillBackground(False)
        self.image3Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image3Label.setText("")
        #self.image3Label.setPixmap(QtGui.QPixmap("D:/A02.2020-08-27-20-07-49/A02_Bottom Slide_R_p01_0_A01f00d0.TIF"))
        self.image3Label.setScaledContents(True)
        self.image3Label.setObjectName("image3Label")
        self.tabWidget.addTab(self.tab2, "")
        
        self.totalcountLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.totalcountLineEdit.setGeometry(QtCore.QRect(648, 529, 71, 22))
        self.totalcountLineEdit.setReadOnly(True)
        self.totalcountLineEdit.setObjectName("totalcountLineEdit")
        
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(577, 529, 71, 20))
        self.label3.setObjectName("label3")
        
        self.image1Label.raise_()
        self.watershedButton.raise_()
        self.filepathTextEdit.raise_()
        self.label1.raise_()
        self.min_distanceSpinBox.raise_()
        self.label2.raise_()
        self.tabWidget.raise_()
        self.totalcountLineEdit.raise_()
        self.label3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionOpen.triggered.connect(lambda: self.openClicked())
        self.watershedButton.clicked.connect(self.watershedClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Watershed GUI"))
        self.watershedButton.setText(_translate("MainWindow", "Watershed"))
        self.label1.setText(_translate("MainWindow", "File path"))
        self.label2.setText(_translate("MainWindow", "min_distance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Labeled by number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Labeled by color"))
        self.label3.setText(_translate("MainWindow", "Total count"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a new file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def openClicked(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        self.filepathTextEdit.setPlainText(self.path)
        self.img = cv2.imread(self.path, cv2.IMREAD_ANYDEPTH)
        self.img = (self.img/4095)*255
        self.img = np.uint8(self.img)
        #cv2.imshow("img", self.img)
        self.imgGUI = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_Indexed8)
        self.image1Label.setPixmap(QtGui.QPixmap.fromImage(self.imgGUI))
        
    def watershedClicked(self):
        labeledImg = copy.deepcopy(self.img)
        thresh = cv2.threshold(labeledImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresh2 = cv2.threshold(labeledImg, 20, 255, cv2.THRESH_BINARY)[1]
        thresh = thresh & thresh2;
        D = ndimage.distance_transform_edt(thresh)
        localMax = peak_local_max(D, indices=False, min_distance=self.min_distanceSpinBox.value(), labels=thresh)
        markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
        labels = watershed(-D, markers, mask=thresh)
        
        for label in np.unique(labels):
	
            if label == 0:
                continue
		
            mask = np.zeros(labeledImg.shape, dtype="uint8")
            mask[labels == label] = 255
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)
            ((x, y), r) = cv2.minEnclosingCircle(c) 
            cv2.circle(labeledImg, (int(x), int(y)), int(r), (255, 255, 255), 1) 
            cv2.putText(labeledImg, "#{}".format(label), (int(x) - 10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        #cv2.imshow("out", labeledImg)        
        self.imgGUI2 = QtGui.QImage(labeledImg.data, labeledImg.shape[1], labeledImg.shape[0], QtGui.QImage.Format_Indexed8)
        self.image2Label.setPixmap(QtGui.QPixmap.fromImage(self.imgGUI2))
        
        self.totalcountLineEdit.setText(str(labels.max()))
        
        colorLabeledImg = color.label2rgb(labels, bg_label=0)
        colorLabeledImg = 255*colorLabeledImg
        colorLabeledImg = colorLabeledImg.astype(np.uint8)
        #cv2.imshow("color", colorLabeledImg)
        self.imgGUI3 = QtGui.QImage(colorLabeledImg.data, colorLabeledImg.shape[1], colorLabeledImg.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image3Label.setPixmap(QtGui.QPixmap.fromImage(self.imgGUI3))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

