from PyQt6.QtWidgets import *
import database_islemleri.veri_alma as di #bu bağlantı müşteri görüntülemek için
#-------- login ekranı --------------
import musteri_goruntu.musteri_gor as mg

class Mainwindow(QMainWindow):
#login ekranı
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
        giris_button.clicked.connect(self.AnaMenuAc) # butona tıkayınca 

        # giris_button.setFixedWidth(100)
        #---------------------------------
        #----------- Qwidget ile pencere-------
        container = QWidget()
        container.setLayout(cont_login_main)
        self.setCentralWidget(container)


    def AnaMenuAc(self):
        self.close()
        self.anaMenu = AnaMenu()
        self.anaMenu.show()
        ### ####


#------------------- ikinci ekran ------------------------
class AnaMenu(QMainWindow):
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
        # self.close()
        self.musteri = MusteriGoruntule()
        self.musteri.show()

    
    def siparisTakipEt(self):
        pass


class MusteriGoruntule(QMainWindow):
#aranacak kişini girdisini alan pencereyi yapan metod
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Musteri Arama")

        icerik = QVBoxLayout() #main window

        icerik.addWidget(QLabel("Müsteri Adı: ")) #müşteri adı
        self.aranan = QLineEdit()
        icerik.addWidget(self.aranan)
        self.veri = self.aranan.text()

        arama_btn = QPushButton("Ara") #arama butonu
        icerik.addWidget(arama_btn)
        arama_btn.clicked.connect(self.kullaniciBilgiAl)
        
#aranan isimin bilgilerini yazdır

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

#kullanıcı bilgilerini database'den alan metod
    def kullaniciBilgiAl(self): #burada kaldım
        aranan_text = self.aranan.text() #bilgiyi ekrana yazıyor.
        print(aranan_text) ### 

        self.kullanici_bilgisi = di.kullaniciVeriAl(aranan_text)# 
        print(self.kullanici_bilgisi)
        
        self.musteri_bilgi_yolla() #degisti1

#data yollama metodu
    def musteri_bilgi_yolla(self):
        data_tran.receive_data(self.kullanici_bilgisi)
        self.close()
        #musteri bilgisi açılıyor.
        self.musteriBilgiEkrani = MusteriBilgisi() 
        self.musteriBilgiEkrani.show()


class MusteriBilgisi(QMainWindow):
#musteri bilgisi ekranı
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Musteri Bilgisi")

        self.kullanici_bilgisi = data_tran.data1
        print(self.kullanici_bilgisi)

        self.adi = self.kullanici_bilgisi[0][1] # 0 liste içindeki tuple'nı
        self.soyadi = self.kullanici_bilgisi[0][2]
        self.email = self.kullanici_bilgisi[0][4]
        self.telNo = self.kullanici_bilgisi[0][5]
        self.adres = self.kullanici_bilgisi[0][6]

        #------ degiskenleri yazdırma
        self.setWindowTitle("Kullanıcı Bilgileri")
        icerik = QVBoxLayout() #main window

        labelAdi = QLabel("Adı: " + self.adi)
        icerik.addWidget(labelAdi)

        labelSoyadi = QLabel("Soyadı: " + self.soyadi)
        icerik.addWidget(labelSoyadi)

        labelEmail = QLabel("Email: " + self.email)
        icerik.addWidget(labelEmail)

        labelTelNo = QLabel("Tel: " + self.telNo)
        icerik.addWidget(labelTelNo)

        labelAdres = QLabel("Adres: " + self.adres)
        icerik.addWidget(labelAdres)

        button1 = QPushButton("Tamam") #tama butonu
        icerik.addWidget(button1)
        button1.clicked.connect(self.pencereKapat)
        
        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        ###    bu pencere tasarım olarak iyileştirilecek

    def data_al(self, data): #d
        print(data)

    def pencereKapat():
        pass


class DataTransfer():
    def receive_data(self,data="No Data"):
        self.data1 = data
    
    def printer(self):
        print(self.data1, "data transfer")

#class örneği ----------
# data_tran = DataTransfer()
# data_tran.receive_data("google")
# print(data_tran.printer())
# -----------------------------
data_tran = DataTransfer()

mainApp = QApplication([])

mainWin = Mainwindow()
mainWin.show()

mainApp.exec()


# di.kullaniciGoruntule()