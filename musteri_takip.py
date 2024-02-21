from PyQt6.QtWidgets import *
import database_islemleri.databaseislem as di #bu bağlantı müşteri görüntülemek için
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
        button1 = QPushButton("Müşteri Bilgileri")
        mainContent.addWidget(button1)
        button1.clicked.connect(self.musteriAc)

        button2 = QPushButton("Sipariş Takip")
        mainContent.addWidget(button2)
        button2.clicked.connect(self.siparisTakipEt)

        window = QWidget()
        window.setLayout(mainContent)
        self.setCentralWidget(window)


    def musteriAc(self): # musteri bilgileri penceresini acar
        self.close()
        self.musteri = MusteriBilgileri()
        self.musteri.show()

    
    def siparisTakipEt(self):
        pass


class MusteriBilgileri(QMainWindow): #ikinci menude
    def __init__(self):
        super().__init__()
        # -----  musteri bilgilerini database'den alma ----
        musteri_bilgisi = di.kullaniciGoruntule() #bu kütüphane bana kullanıcı bilgilerini döndürüyor.

        mainContent = QVBoxLayout() #main container
        mainContent.addWidget(QLabel("Adı"))
        mainContent.addWidget(QLineEdit())
        
        
        # bir bilgiyi ekrana nasıl yazarım?
        #Qlabel deneme yapıyorum 
        #database'den bilgileri alacam
        #sonra qWidget içine koyacağım

        #kullanici_bilgileri = di.kullaniciGoruntule() # di, database islemleri kısaltmasıdır.

        #for x in kullanici_bilgileri:
            # print(x)

    #yeni bir metod kullancağım. bu metod kullanıcı bilgilerini oop ile saklayacak
    def musteriBilgileriYaz(self):




        """
        window = QWidget()
        window.setLayout(mainContent)
        self.setCentralWidget(window)
        """


mainApp = QApplication([])

mainWin = Mainwindow()
mainWin.show()

mainApp.exec()


# di.kullaniciGoruntule()