# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tentang.ui'
#
# Created: Sat Jun 23 10:30:16 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormTentang(object):
    def setupUi(self, FormTentang):
        FormTentang.setObjectName("FormTentang")
        FormTentang.setWindowModality(QtCore.Qt.ApplicationModal)
        FormTentang.resize(400, 300)
        self.tabWidget = QtGui.QTabWidget(FormTentang)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 371, 221))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 341, 161))
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea = QtGui.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 361, 181))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 361, 181))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtGui.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 341, 81))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(158, 129, 201, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/newPrefix/built-with-Qt_Horizontal_Small.png"))
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_3, "")
        self.label = QtGui.QLabel(FormTentang)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(FormTentang)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 141, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(FormTentang)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormTentang)

    def retranslateUi(self, FormTentang):
        FormTentang.setWindowTitle(QtGui.QApplication.translate("FormTentang", "Tentang", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("FormTentang", "<html><head/><body><p>Aplikasi<br/>(c) 2018 Muhammad Refa<br/><a href=\"https://github.com/muhammadrefa\"><span style=\" text-decoration: underline; color:#2980b9;\">GitHub</span></a></p><p align=\"right\">Video (perizinan sedang diurus)<br/>(c) 2013-2017 Fitria Leurima<br/><a href=\"https://www.youtube.com/user/FitriaKN\"><span style=\" text-decoration: underline; color:#2980b9;\">YouTube</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("FormTentang", "Aplikasi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("FormTentang", "<html><head/><body><p align=\"justify\">SIBI (Sistem Isyarat Bahasa Indonesia)</p><p align=\"justify\">Merupakan bahasa isyarat yang diciptakan oleh Alm. Anton Widyatmoko mantan kepala sekolah SLB/B Widya Bakti Semarang bekerjasama dengan mantan kepala sekolah SLB/B di Jakarta dan Surabaya</p><p>Sumber : https://www.selasar.com/jurnal/13935/Eksistensi-Bahasa-Isyarat-Indonesia-(BISINDO)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("FormTentang", "SIBI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("FormTentang", "<html><head/><body><p>Dibuat menggunakan PySide, Qt dan Python</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("FormTentang", "Teknologi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FormTentang", "Kamus SIBI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FormTentang", "v0.1 pre-alpha", None, QtGui.QApplication.UnicodeUTF8))

# import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FormTentang = QtGui.QWidget()
    ui = Ui_FormTentang()
    ui.setupUi(FormTentang)
    FormTentang.show()
    sys.exit(app.exec_())

