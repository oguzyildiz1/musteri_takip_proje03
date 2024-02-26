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

        button2 = QPushButton("Müşteri Ekle")
        mainContent.addWidget(button2)
        button2.clicked.connect(self.musteriEkle)

        window = QWidget()
        window.setLayout(mainContent)
        self.setCentralWidget(window)


    def musteriAc(self): # musteri bilgileri penceresini acar
        # self.close()
        self.musteri = MusteriGoruntule()
        self.musteri.show()

    
    def musteriEkle(self):
        self.musteriEk = MusteriEkleme()
        self.musteriEk.show()


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

        self.kullanici_bilgisi = di.kullaniciVeriAl(aranan_text)# 
        
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
        # print(self.kullanici_bilgisi)

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

    def pencereKapat(self):
        self.close()

#----- musteri ekleme penceresi -----------
#amac: kayıt alıp, veri tabanına ekleme
class MusteriEkleme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Müsteri Ekle")

        musEklePen = QVBoxLayout()
        
# ---------- widgetları ekleme start --------
        musEklePen.addWidget(QLabel("Adı"))
        self.adi_info = QLineEdit()
        musEklePen.addWidget(self.adi_info)
        musEklePen.addWidget(QLabel("Soyadı"))
        self.soyadi_info = QLineEdit()
        musEklePen.addWidget(self.soyadi_info)
        musEklePen.addWidget(QLabel("Şifre"))
        self.sifre_info = QLineEdit()
        musEklePen.addWidget(self.sifre_info)
        musEklePen.addWidget(QLabel("E-Mail"))
        self.email_info = QLineEdit()
        musEklePen.addWidget(self.email_info)
        musEklePen.addWidget(QLabel("Telefon"))
        self.telNo_info = QLineEdit()
        musEklePen.addWidget(self.telNo_info)
        musEklePen.addWidget(QLabel("Adres"))
        self.adres_info = QLineEdit()
        musEklePen.addWidget(self.adres_info)
        self.but_ekle = QPushButton("Ekle")
        musEklePen.addWidget(self.but_ekle)
        self.but_ekle.clicked.connect(self.musEkleme)

#-------- veri alma start -----------
        araclar = QWidget()
        araclar.setLayout(musEklePen)
        self.setCentralWidget(araclar)

    
    def musEkleme(self):
        self.adi_veri = self.adi_info.text()
        self.soyadi_veri = self.soyadi_info.text()
        self.sifre_veri = self.sifre_info.text()
        self.email_veri = self.email_info.text()
        self.telNo_veri = self.telNo_info.text()
        self.adres_veri = self.adres_info.text()

        musEkLis = [
            self.adi_veri, 
            self.soyadi_veri,
            self.sifre_veri,
            self.email_veri,
            self.telNo_veri,
            self.adres_veri
            ]
        
        basarili = di.kullaniciEkle(musEkLis)
        if basarili:
            self.basarili = BasariliPencere()
            self.basarili.show()

        # print(musEkLis)

#--------- kisi başarılı eklenenince ----------------
class BasariliPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        icerik = QVBoxLayout()

        icerik.addWidget(QLabel("Kişi başarıyla eklendi"))
        tamamBut = QPushButton("Tamam")
        icerik.addWidget(tamamBut)
        tamamBut.clicked.connect(self.penKapat)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)
    
    def penKapat(self):
        self.close()


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