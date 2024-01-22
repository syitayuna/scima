from matematika import *
import matematika as mtk
import sains as sc
import menu
import os

def pergi(nomor):
    global line
    line = nomor

line = 0
while True:
    
    # ---------- MENU UTAMA ----------
    if line == 0:
        os.system("cls")
        menu.main()
        pilih_tema = input("...Pilih tema disini : ")
        if pilih_tema == "1":
            pergi(1)
        elif pilih_tema == "2":
            pergi(5)
        else:
            os.system('cls')

    # --------- SUB MENU TEMA MATEMATIKA ----------
    elif line == 1:
        os.system("cls")
        menu.math()
        pilih_matematika = input("Tulis pilihanmu disini : ")
        if pilih_matematika == '1':
            pergi(2)
        elif pilih_matematika == "2":
            pergi(3)
        elif pilih_matematika == "3":
            pergi(4)
        elif pilih_matematika == '00':
            pergi(0)
        else:
            pergi(1)

    # --------- SUBTEMA MATEMATIKA TEOREMA PHYTAGORAS ----------
    elif line == 2:
        os.system("cls")
        menu.rumteo()
        nilai = input("Tulis disini : ").lower()
        if nilai in ("sisi miring", "miring"):
            sisi_miring.miring(cara_teorema)
            pergi(6)
        elif nilai in ("sisi alas", "alas"):
            sisi_alas.alas(cara_teorema)
            pergi(6)
        elif nilai in ("sisi tegak", "tegak"):
            sisi_tegak.tegak(cara_teorema)
            pergi(6)

    # --------- SUBTEMA MATEMATIKA BANGUN RUANG 3 DIMENSI ----------
    elif line == 3:
        os.system("cls")
        menu.menu_ruang()
        ruang = input("Tulis disini : ").lower()
        if ruang == "mencari volume kubus":
            volume_kubus.volume(cara_kubus)
            pergi(6)
        elif ruang == "mencari luas kubus":
            luas_kubus.luas(cara_kubus)
            pergi(6)
        elif ruang == "mencari volume balok":
            volume_balok.volume(cara_balok)
            pergi(6)
        elif ruang == "mencari luas balok":
            luas_balok.luas(cara_balok)
            pergi(6)
        elif ruang == "mencari volume bola":
            volume_bola.volume(cara_bola)
            pergi(6)
        elif ruang == "mencari luas bola":
            luas_bola.luas(cara_bola)
            pergi(6)
        else:
            pergi(3)

    # --------- SUBTEMA MATEMATIKA BARISAN DAN DERET ARITMATIKA ----------
    elif line == 4:
        os.system("cls")
        menu.aritmatika()
        cari = input("Tulis disini : ").lower().split()
        if "suku" and "ke" in cari:
            mtk.barisan(cari)
            pergi(6)
        elif "jumlah" and "suku" in cari:
            mtk.deret(cari)
            pergi(6)
        else:
            pergi(4)

    # --------- SUB MENU TEMA SAINS FISIKA ----------
    elif line == 5:
        os.system("cls")
        menu.sains()
        energi = input("Tulis pilihanmu disini : ")
        if energi == "1":
            sc.kinetik()
            pergi(6)
        elif energi == "2":
            menu.REP()
            sc.potensial()
            pergi(6)
        elif energi == "3":
            os.system("cls")
            menu.kimia()
            mencari = input("Apa yang kamu cari : ").lower()
            sc.kimia(mencari)
            pergi(6)
        elif energi == "00":
            pergi(0)
        else:
            pergi(5)

    # --------- MENU PENGULANGAN SEBUAH PROGRAM ----------
    elif line == 6:
        print("\nApakah anda ingin mengulang ?")
        jawab = input("Tulis disini (Ya/Tidak): ").lower()
        if jawab == "ya":
            pergi(0)
        elif jawab == "tidak":
            print("""
            ===========================================
    ------------- SEMOGA HARI HARIMU MENYENANGKAN -------------
            ===========================================
                            """)
            break
        else:
            os.system("cls")
            pergi(6)

    else:
        pergi(0)
        