# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simpleWatershedGUIv2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        MainWindow.resize(1130, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.watershedButton = QtWidgets.QPushButton(self.centralwidget)
        self.watershedButton.setGeometry(QtCore.QRect(570, 520, 141, 41))
        self.watershedButton.setObjectName("watershedButton")
        
        self.filepathTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.filepathTextEdit.setEnabled(True)
        self.filepathTextEdit.setGeometry(QtCore.QRect(20, 40, 531, 31))
        self.filepathTextEdit.setReadOnly(True)
        self.filepathTextEdit.setObjectName("filepathTextEdit")
        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.path_label.setObjectName("path_label")
        
        self.image1Label = QtWidgets.QLabel(self.centralwidget)
        self.image1Label.setGeometry(QtCore.QRect(20, 80, 531, 435))
        self.image1Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image1Label.setAutoFillBackground(False)
        self.image1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image1Label.setText("")
        #self.image1Label.setPixmap(QtGui.QPixmap("D:/A02.2020-08-27-20-07-49/A02_Bottom Slide_R_p01_0_A01f00d0.TIF"))
        self.image1Label.setScaledContents(True)
        self.image1Label.setObjectName("image1Label")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(570, 55, 531, 461))
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.image4Label = QtWidgets.QLabel(self.tab3)
        self.image4Label.setGeometry(QtCore.QRect(0, 0, 531, 435))
        self.image4Label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image4Label.setAutoFillBackground(False)
        self.image4Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image4Label.setText("")
        #self.image4Label.setPixmap(QtGui.QPixmap("D:/A02.2020-08-27-20-07-49/A02_Bottom Slide_R_p01_0_A01f00d0.TIF"))
        self.image4Label.setScaledContents(True)
        self.image4Label.setObjectName("image4Label")
        self.tabWidget.addTab(self.tab3, "")
        
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
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 530, 149, 24))
        self.widget.setObjectName("widget")
        
        self.threshold_horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.threshold_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.threshold_horizontalLayout.setObjectName("threshold_horizontalLayout")
        self.threshold_label = QtWidgets.QLabel(self.widget)
        self.threshold_label.setObjectName("threshold_label")
        self.threshold_horizontalLayout.addWidget(self.threshold_label)
        self.thresholdSpinBox = QtWidgets.QSpinBox(self.widget)
        self.thresholdSpinBox.setMinimum(0)
        self.thresholdSpinBox.setProperty("value", 5)
        self.thresholdSpinBox.setObjectName("thresholdSpinBox")
        self.threshold_horizontalLayout.addWidget(self.thresholdSpinBox)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(380, 530, 124, 24))
        self.widget1.setObjectName("widget1")
        self.min_dist_horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.min_dist_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.min_dist_horizontalLayout.setObjectName("min_dist_horizontalLayout")
        self.min_dist_label = QtWidgets.QLabel(self.widget1)
        self.min_dist_label.setObjectName("min_dist_label")
        self.min_dist_horizontalLayout.addWidget(self.min_dist_label)
        self.min_distanceSpinBox = QtWidgets.QSpinBox(self.widget1)
        self.min_distanceSpinBox.setMinimum(1)
        self.min_distanceSpinBox.setProperty("value", 10)
        self.min_distanceSpinBox.setObjectName("min_distanceSpinBox")
        self.min_dist_horizontalLayout.addWidget(self.min_distanceSpinBox)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(220, 530, 130, 24))
        self.widget2.setObjectName("widget2")
        self.denoise_horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.denoise_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.denoise_horizontalLayout.setObjectName("denoise_horizontalLayout")
        self.denoise_label = QtWidgets.QLabel(self.widget2)
        self.denoise_label.setObjectName("denoise_label")
        self.denoise_horizontalLayout.addWidget(self.denoise_label)
        self.denoiseSpinBox = QtWidgets.QSpinBox(self.widget2)
        self.denoiseSpinBox.setMinimum(1)
        self.denoiseSpinBox.setProperty("value", 10)
        self.denoiseSpinBox.setObjectName("denoiseSpinBox")
        self.denoise_horizontalLayout.addWidget(self.denoiseSpinBox)
        self.denoise_label.raise_()
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(730, 530, 151, 24))
        self.widget3.setObjectName("widget3")
        self.totalcount_horizontalLayout = QtWidgets.QHBoxLayout(self.widget3)
        self.totalcount_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.totalcount_horizontalLayout.setObjectName("totalcount_horizontalLayout")
        self.totalcount_label = QtWidgets.QLabel(self.widget3)
        self.totalcount_label.setObjectName("totalcount_label")
        self.totalcount_horizontalLayout.addWidget(self.totalcount_label)
        self.totalcountLineEdit = QtWidgets.QLineEdit(self.widget3)
        self.totalcountLineEdit.setReadOnly(True)
        self.totalcountLineEdit.setObjectName("totalcountLineEdit")
        self.totalcount_horizontalLayout.addWidget(self.totalcountLineEdit)
        self.image1Label.raise_()
        self.watershedButton.raise_()
        self.filepathTextEdit.raise_()
        self.path_label.raise_()
        self.min_distanceSpinBox.raise_()
        self.min_dist_label.raise_()
        self.tabWidget.raise_()
        self.totalcountLineEdit.raise_()
        self.totalcount_label.raise_()
        self.denoiseSpinBox.raise_()
        self.denoise_label.raise_()
        self.thresholdSpinBox.raise_()
        self.threshold_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1130, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.actionOpen.triggered.connect(lambda: self.openClicked())
        self.watershedButton.clicked.connect(self.watershedClicked)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Watershed GUI"))
        self.watershedButton.setText(_translate("MainWindow", "Watershed"))
        self.path_label.setText(_translate("MainWindow", "File path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Mask"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Labeled by number"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Labeled by color"))
        self.threshold_label.setText(_translate("MainWindow", "threshold percent"))
        self.min_dist_label.setText(_translate("MainWindow", "min_distance"))
        self.denoise_label.setText(_translate("MainWindow", "denoise factor"))
        self.totalcount_label.setText(_translate("MainWindow", "Total count"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a new file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))

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
        thresh2 = cv2.threshold(labeledImg, self.thresholdSpinBox.value()*2.55, 255, cv2.THRESH_BINARY)[1]
        thresh = thresh & thresh2;
        arr_size = self.denoiseSpinBox.value()
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (arr_size, arr_size))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        D = ndimage.distance_transform_edt(thresh)
        localMax = peak_local_max(D, indices=False, min_distance=self.min_distanceSpinBox.value(), labels=thresh)
        markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
        labels = watershed(-D, markers, mask=thresh)
        
        thresh = 255*thresh
        self.imgGUI4 = QtGui.QImage(thresh.data, thresh.shape[1], thresh.shape[0], QtGui.QImage.Format_Indexed8)
        self.image4Label.setPixmap(QtGui.QPixmap.fromImage(self.imgGUI4))
        
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

