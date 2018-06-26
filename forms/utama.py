# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utama.ui'
#
# Created: Wed Jun 27 00:18:00 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 570)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_kategori = QtGui.QListWidget(self.centralwidget)
        self.list_kategori.setGeometry(QtCore.QRect(20, 100, 141, 261))
        self.list_kategori.setObjectName("list_kategori")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 59, 18))
        self.label.setObjectName("label")
        self.list_item = QtGui.QListWidget(self.centralwidget)
        self.list_item.setGeometry(QtCore.QRect(200, 100, 141, 261))
        self.list_item.setObjectName("list_item")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 80, 59, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 220, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.webview = QWebView(self.centralwidget)
        self.webview.setGeometry(QtCore.QRect(370, 10, 880, 500))
        self.webview.setUrl(QtCore.QUrl("about:blank"))
        self.webview.setObjectName("webview")
        self.btn_tampil = QtGui.QPushButton(self.centralwidget)
        self.btn_tampil.setGeometry(QtCore.QRect(250, 370, 88, 34))
        self.btn_tampil.setObjectName("btn_tampil")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 429, 321, 71))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 321, 71))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_deskripsi = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_deskripsi.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_deskripsi.setObjectName("label_deskripsi")
        self.horizontalLayout.addWidget(self.label_deskripsi)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_butir = QtGui.QLabel(self.centralwidget)
        self.label_butir.setGeometry(QtCore.QRect(20, 410, 321, 18))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_butir.setFont(font)
        self.label_butir.setObjectName("label_butir")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 30))
        self.menubar.setObjectName("menubar")
        self.menuTentang = QtGui.QMenu(self.menubar)
        self.menuTentang.setObjectName("menuTentang")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTentang.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Kamus SIBI", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Kategori", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Butir", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_tampil.setText(QtGui.QApplication.translate("MainWindow", "Tampilkan", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Kamus SIBI</span><br/>(Sistem Isyarat Bahasa Indonesia)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_deskripsi.setText(QtGui.QApplication.translate("MainWindow", "Deskripsi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_butir.setText(QtGui.QApplication.translate("MainWindow", "Kategori -> Butir", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTentang.setTitle(QtGui.QApplication.translate("MainWindow", "Te&ntang", None, QtGui.QApplication.UnicodeUTF8))

# from QtWebEngineWidgets.QWebEngineView import QWebEngineView
from PySide.QtWebKit import QWebView

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

