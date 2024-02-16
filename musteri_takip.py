from PyQt6.QtWidgets import *

#-------- login ekranı --------------
class Mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Ekranı")
        # self.setFixedWidth(400)
        # self.setFixedHeight(200)

        # -------------- genel box tanımları ------------
        cont_login_main = QVBoxLayout() #genel container
        cont_adi = QHBoxLayout()
        cont_soyadi = QHBoxLayout()
        cont_sifre = QHBoxLayout()

        #----------------- Adı kısmı -----------
        cont_adi.addWidget(QLabel("Adı")) #adı kısmı
        adi_info = QLineEdit() #adi bilgisi
        adi_info.setFixedWidth(100)
        cont_adi.addWidget(adi_info)
    
        cont_login_main.addLayout(cont_adi)
        # -------------------------

        #------------------- soyadı kısmı---------------
        cont_soyadi.addWidget(QLabel("Soyadı")) #soyadi kısmı
        soyadi_info = QLineEdit() #soyadi bilgisi
        soyadi_info.setFixedWidth(100)
        cont_soyadi.addWidget(soyadi_info)

        cont_login_main.addLayout(cont_soyadi)
        #--------

        #-------------- sifre kısmı ----------------------
        cont_sifre.addWidget(QLabel("Sifre")) #sifre kısmı
        sifre_info = QLineEdit() #soyadi bilgisi
        sifre_info.setFixedWidth(100)
        cont_sifre.addWidget(sifre_info)

        cont_login_main.addLayout(cont_sifre)
        #------------------------------------

        #----------- button ------------------
        giris_button = QPushButton("Giriş")
        cont_login_main.addWidget(giris_button)
        giris_button.clicked.connect(self.siparisMenuAc) # butona tıkayınca 

        # giris_button.setFixedWidth(100)
        #---------------------------------
        #----------- Qwidget ile pencere-------
        container = QWidget()
        container.setLayout(cont_login_main)
        self.setCentralWidget(container)


    def siparisMenuAc(self):
        self.close()
        self.siparisMenu = SiparisMenu()
        self.siparisMenu.show()
        ### ####


#------------------- ikinci ekran ------------------------
class SiparisMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        mainContent = QVBoxLayout()
        button1 = QPushButton("Sipariş Ver")
        mainContent.addWidget(button1)
        button1.clicked.connect(self.siparisVer)

        button2 = QPushButton("Sipariş Takip")
        mainContent.addWidget(button2)
        button2.clicked.connect(self.siparisTakipEt)

        window = QWidget()
        window.setLayout(mainContent)
        self.setCentralWidget(window)


    def siparisVer(self):
        self.siparis = Siparisprogrami()
        self.siparis.show()

    
    def siparisTakipEt(self):
        pass


class Siparisprogrami(QMainWindow):
    def __init__(self):
        super().__init__()

        mainContent = QVBoxLayout()
        mainContent.addWidget(QLabel("Sipariş Ver"))

        window = QWidget()
        window.setLayout(mainContent)
        self.setCentralWidget(window)


print("AD")

mainApp = QApplication([])

mainWin = Mainwindow()
mainWin.show()

mainApp.exec()