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

def test(para1):        
    kulVeriList = para1

    sql = 'INSERT INTO musteriler (ADI, SOYADI, SIFRE, EMAIL, PHONE, ADRES) VALUES (%s, %s, %s, %s, %s, %s)' 

    val = (kulVeriList[0], kulVeriList[1], kulVeriList[2], kulVeriList[3], kulVeriList[4], kulVeriList[5])
    
    mycursor.execute(sql, val)
    mydb.commit()



list1 = ["Selami", "Yıldız", "87964", "selami@hotmail.com","5369874521","Tokat"]

test(list1)