from PyQt6.QtWidgets import *
import sys
import os

simdiki_klasor = os.getcwd() #simdiki klasor yolunu donduruyor

sys.path.append(simdiki_klasor) #alttaki kütüphaneyi import etmek icin bu komut kullanılıyor...

# sys.path.append('C:/Users/yildi/OneDrive/Desktop/python/vektorelBilisim/github/musteri_takip_proje03')

import database_islemleri.veri_alma as di
# import musteri_takip as mt

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
        
        self.kullaniciBilgiEkrani()

# kullanıcı bilgilerini ekrana basan pencereyi yapan metod
    def kullaniciBilgiEkrani(self): 
        # self.setWindowTitle("Musteri Bilgileri")

        #tuple'daki verileri değişkenlere atama
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

    def pencereKapat(self):
        self.close()
        

def calistir():
    # mainApp = QApplication([])

    mainWin = MusteriGoruntule()
    mainWin.show()

    # mainApp.exec()
