#*---------------------------------------------------------------------------------------------------------------------
#**
#***
#****
#*****
#******
#*******
#********                   -------------------------------------------------------------
#*********                  --DI BUAT OLEH : IDA BAGUS PUTU DHARMA SANTYA(Gusde Dharma)--
#*********                  --                       MR-EXEC                           --
#********                   -------------------------------------------------------------
#*******
#******
#*****
#****
#***
#**
#*
#Database Connect------------------------------------------------------------------------------------------------------
import mysql.connector
import os
import time
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="nilai"
)
#input orang yg lulus -------------------------------------------------------------------------------------------------
def nilailulus(db):
    print("Masukan Data Peserta")
    data1 = input("Masukan NIS :")
    data2 = input("Masukan Nama :")
    data3 = input("Masukan Mapel :")
    data4 = int(input("Masukan Nilai :"))
    data5 = (data1, data2, data3, data4)
    cursor = db.cursor()
    if data4 in range(0,100):
        try:
            sql = "INSERT INTO siswa (NIS, NAMA, MAPEL, NILAI) VALUES(%s, %s, %s, %s)"
            while data4 > 100:
                exit("Maaf Input Melebihi Maximal 100")
            while data4 < 0:
                exit("Maaf Input Melebihi Minimum 0")
            cursor.execute(sql, data5)
            db.commit()
            print("{} Data berhasil di masukan".format(cursor.rowcount))
        except KeyboardInterrupt:
            exit("[Exit]Keybord Interrupt")

    else:
        print("Maaf Input Salah")
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#melihat data yg lulus ------------------------------------------------------------------------------------------------
def lihatdatalulus(db):
    cursor = db.cursor()
    sql = "SELECT * FROM siswa WHERE NILAI >75"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
#melihat data yg tidak lulus ------------------------------------------------------------------------------------------
def lihatdatanolulus(db):
    cursor = db.cursor()
    sql = "SELECT * FROM siswa WHERE NILAI <75"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
#update data ----------------------------------------------------------------------------------------------------------
def updatedatalulus(db):
    print("Update Data Yg Tidak Remidial")
    cursor = db.cursor()
    lihatdatalulus(db)
    data1b = input("Masukan Nis siswa :")
    data2b = input("Masukan Mapel Baru :")
    data3b = input("Masukan Nilai Baru :")
    sql = "UPDATE siswa SET MAPEL=%s, NILAI=%s WHERE NIS=%s"
    val = (data2b, data3b, data1b)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data berhasil di UPDATE".format(cursor.rowcount))
    lihatdatalulus(db)
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
# update data tdk lulus -----------------------------------------------------------------------------------------------
def updatedatanolulus(db):
    print("Update Data Yg Remedial")
    cursor = db.cursor()
    lihatdatanolulus(db)
    data1c = input("Masukan Nis siswa :")
    data2c = input("Masukan Mapel Baru :")
    data3c = input("Masukan Nilai Baru :")
    sql = "UPDATE siswa SET MAPEL=%s, NILAI=%s WHERE NIS=%s"
    val = (data2c, data3c, data1c)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data berhasil di UPDATE".format(cursor.rowcount))
    lihatdatanolulus(db)
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#Cari data lulus ------------------------------------------------------------------------------------------------------
def caridatalulus(db):
    print("Cari Data Cepat Yg Tidak Remidial")
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql4 = "SELECT * FROM siswa WHERE NIS LIKE %s OR NAMA LIKE %s"
    val4 = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql4, val4)
    results = cursor.fetchall()
    print("Ini hasil pencarian anda :")
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#Cari Data yg tidak lulus ---------------------------------------------------------------------------------------------
def caridatatdklulus(db):
    print("Cari Data Cepat Yg Remidial")
    cursor = db.cursor()
    keyword = input("Kata kunci: ")
    sql4 = "SELECT * FROM nolulus WHERE NIS LIKE %s OR NAMA LIKE %s"
    val4 = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql4, val4)
    results = cursor.fetchall()
    print("Ini hasil pencarian anda :")

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#Delete Data yang lulus -----------------------------------------------------------------------------------------------
def deletelulus(db):
    print("Delete Data Yg Tidak Remedial")
    cursor = db.cursor()
    lihatdatalulus(db)
    no = input("Pilih NIS data yg mau di DELETE :")
    sql = "DELETE FROM siswa WHERE NIS=%s"
    val = (no,)
    cursor.execute(sql, val)
    db.commit()
    ("{} Data Telah di DELETE".format(cursor.rowcount))
# Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#Delete Data yang tdklulus --------------------------------------------------------------------------------------------
def deletetdklulus(db):
    print("Delete Data Yg Remidial")
    cursor = db.cursor()
    lihatdatanolulus(db)
    no = input("Pilih NIS data yg mau di DELETE :")
    sql = "DELETE FROM siswa WHERE NIS=%s"
    val = (no,)
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Telah di DELETE".format(cursor.rowcount))
#Pemilihan Kembali ke Menu---------------------------------------------------------------------------------------------
    print("Apakah anda ingin kembali ke menu [Y/N]")
    print("Y. untuk kembali ke Menu semula")
    print("N. Untuk Keluar")
    menu = str(input("Masukan pilihan anda :"))
    if menu == None:
        print("Anda Harus Memasukan Input")
        exit("")
    else:
        pass
    if menu == "Y":
        os.system("cls")
        Menu()
    else:
        if menu == "N":
            exit("Terima kasih")
        else:
            print("Maaf input yang anda masukan salah")
#Menu Pemilihan -------------------------------------------------------------------------------------------------------
def Menu():
    print("\33[31m-----------------------------------------------------------------\33[31m")
    print("\33[1;34m----   Tools Membatu Guru Memasukan Daftar Nilai Harian      ----\33[1;31m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("\33[33m-----------------------------------------------------------------\33[33m")
    print("\33[1;34m----                 create by 90s Rabbits                   ----\33[1;34m")
    print("\33[30m-----------------------------------------------------------------\33[30m")
    print("1.__Masukan Data Orang Yg Ikut Ulangan")
    print("2.__Lihat Data Orang Yg Tidak Remidial")
    print("3.__Lihat Data Orang Yg Remidial")
    print("4.__Update Data Orang Yg Tidak Remidial")
    print("5.__Update Data Orang Yg Remidial")
    print("6.__Cari Data Cepat Yg Tidak Remidial")
    print("7.__Cari Data Cepat Yg Remidial")
    print("8.__Delete Data Orang Yg Tidak Remidial")
    print("9.__Delete Data Orang Yg Remidial")
    print("0.__Keluar")
#Program Menu
    menu = input("Masukan Menu Yg Akan Di Pilih :")
    if menu == "1":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        nilailulus(db)
    elif menu == "2":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        lihatdatalulus(db)
    elif menu == "3":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        lihatdatanolulus(db)
    elif menu == "4":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        updatedatalulus(db)
    elif menu == "5":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        updatedatanolulus(db)
    elif menu == "6":
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        os.system("cls")
        caridatalulus(db)
    elif menu == "7":
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        os.system("cls")
        caridatatdklulus(db)
    elif menu == "8":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        deletelulus(db)
    elif menu == "9":
        os.system("cls")
        if menu == None:
            print("Anda Harus Memasukan Input")
            exit("")
        else:
            pass
        deletetdklulus(db)
    elif menu == "0":
        os.system("cls")
        exit("Terima Kasih")
    else:
        print("Maaf Input Salah")
#----------------------------------------------------------------------------------------------------------------------
Menu()


