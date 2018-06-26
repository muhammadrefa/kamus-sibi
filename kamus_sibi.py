import sys, os
# from PyQt5 import QtCore, QtGui, QtWidgets
from PySide import QtGui, QtCore
from forms.utama import Ui_MainWindow
from forms.tentang import Ui_FormTentang

class firstGUI(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # Ui_MainWindow.__init__(self)
        # self.setupUi(dialog)
        super(firstGUI, self).__init__(parent)
        self.setupUi(self)

        self.statusbar.showMessage("Mohon tunggu...")

        self.webview.load("./data/mohon.html")

        kategori = []
        self.butir = []

        kategori.append("Alfabet")
        self.butir.append(["A", "B", "C", "D", "E", "F", "G"])

        kategori.append("Keluarga")
        self.butir.append(
            ["Ayah", "Ibu", "Anak", "Adik", "Kakak", "Kakek", "Nenek", "Bibi (Tante)", "Paman (Om)", "Suami", "Istri",
             "Cucu", "Bayi"])

        self.list_kategori.addItems(kategori)
        self.list_kategori.currentItemChanged.connect(self.kategori_dipilih)
        self.list_item.currentItemChanged.connect(self.item_dipilih)
        self.btn_tampil.clicked.connect(self.tampil)
        self.menuTentang.aboutToShow.connect(self.funcTentang)

        self.statusbar.showMessage("Siap! Pilih kategori dan butir, lalu klik 'Tampilkan'")

    def kategori_dipilih(self):
        kategori = self.list_kategori.currentItem().text()
        self.webview.load("./data/mohon.html")
        self.label_butir.setText(kategori + " -> ")
        self.label_deskripsi.setText("")
        self.statusbar.showMessage("Siap! Pilih kategori dan butir, lalu klik 'Tampilkan' untuk menampilkan video")
        self.list_item.clear()
        try:
            self.list_item.addItems(self.butir[self.list_kategori.currentRow()])
        except:
            pass

    def item_dipilih(self):
        kategori = self.list_kategori.currentItem().text()
        item = self.list_item.currentItem().text()
        self.webview.load("./data/mohon.html")
        self.label_butir.setText(kategori + " -> " + item)
        self.label_deskripsi.setText("Deskripsi untuk " + kategori + " -> " + item)
        self.statusbar.showMessage("Siap! Pilih kategori dan butir, lalu klik 'Tampilkan' untuk menampilkan video")

    def tampil(self):
        try:
            kategori = self.list_kategori.currentItem().text()
            item = self.list_item.currentItem().text()
            # print(self.list_kategori.currentItem().text() + " -> " + self.list_item.currentItem().text())
            print(kategori + " -> " + item)
            self.label_butir.setText(kategori + " -> " + item)
            berkas_video = "./data/video_sibi/" + kategori + "/" + item + ".mp4"
            if os.path.isfile(berkas_video):
                self.webview.load(berkas_video)
                self.statusbar.showMessage("Menampilkan video untuk " + kategori + " -> " + item)
            else:
                self.statusbar.showMessage("Galat! Video tidak ditemukan")
        except:
            print("GALAT")

    def funcTentang(self):
        appPos = self.pos()
        print("x -> " + str(appPos.x()) + " y -> " + str(appPos.y()))
        self.tentang = windowTentang()
        self.tentang.move(appPos.x()+(self.tentang.width()/2), appPos.y()+(self.tentang.height()/2))
        self.tentang.show()

class windowTentang(QtGui.QWidget, Ui_FormTentang):
    def __init__(self, parent=None):
        super(windowTentang, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    print(os.getcwd())
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()

    app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    # prog = firstGUI(MainWindow)
    # MainWindow.show()

    prog = firstGUI()
    prog.show()

    sys.exit(app.exec_())