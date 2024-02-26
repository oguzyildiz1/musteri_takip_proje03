import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "123456",
        database = "novartis"
    )

    mycursor = mydb.cursor()
    print("Bağlandı...")

except:
    print("Bağlantı sorunu")

"""
def kullaniciEkle():
    sql = "INSERT INTO musteriler (ADI, SOYADI, SIFRE, EMAIL, PHONE, ADRES) VALUES (%s, %s, %s, %s, %s, %s)"

    val = ("Orhan", "Yıldız", "4512", "oyıl@gmail.com", "5336541298", "İstanbul")

    mycursor.execute(sql, val)
    mydb.commit()
"""

def kullaniciVeriAl(para1):
    try:

        girdi = para1 #ad geldi

        sql = 'SELECT * FROM musteriler WHERE ADI = "%s"' % girdi #aranan adı
        # sql = 'SELECT * FROM musteriler WHERE ADI = "Oğuzhan"' % girdi #aranan adı

        mycursor.execute(sql)
        result = mycursor.fetchall()

        return result #arana kişini tüm verilerini döndürür

    except:
        print("Görüntülenme hatası!")


def kullaniciEkle(para1):
    try:
        kulVeriList = para1
        sql = 'INSERT INTO musteriler (ADI, SOYADI, SIFRE, EMAIL, PHONE, ADRES VALUES (%s, %s, %s, %s, %s, %s)' % kulVeriList[0], kulVeriList[1], kulVeriList[2], kulVeriList[3],kulVeriList[4], kulVeriList[5]

        mycursor.execute(sql)
        mydb.commit()

    except:
        print("Veri ekleme hatası")
