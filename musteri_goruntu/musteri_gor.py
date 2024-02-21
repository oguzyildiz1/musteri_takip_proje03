from PyQt6.QtWidgets import *

class MusteriGoruntule(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Musteri Bilgileri")

            icerik = QVBoxLayout()

            icerik.addWidget(QLabel("Müsteri Adı: "))
            self.aranan = QLineEdit()
            icerik.addWidget(self.aranan)
            self.veri = self.aranan.text()

            arama_btn = QPushButton("Ara")
            icerik.addWidget(arama_btn)
            arama_btn.clicked.connect(self.bilgiEkrani)
            
            #aranan isimin bilgilerini yazdır

            araclar = QWidget()
            araclar.setLayout(icerik)
            self.setCentralWidget(araclar)

        
        def bilgiEkrani(self):
            aaa = self.aranan.text() #bilgiyi ekrana yazıyor.
            print(aaa)


mainApp = QApplication([])

mainWin = MusteriGoruntule()
mainWin.show()

mainApp.exec()
