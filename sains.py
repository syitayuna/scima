import menu, os, math
from gtts import gTTS
from playsound import playsound
from gtts.tts import gTTSError

def kinetik():
    global energi_kinetik, massa, kecepatan, nilai
    os.system("cls")
    menu.REK()
    nilai = input("Tulis disini : ").lower()
    if nilai in ("energi kinetik", "kinetik"):   
        try:
            massa = int(input("\n..Massa benda (kg)\t      : "))
            kecepatan = int(input("..Kecepatan dari sebuah benda : "))
        except ValueError:
            return kinetik()
        energi_kinetik = 0.5 * massa * (pow(kecepatan, 2))
        caraKinetik()
    elif nilai in ("massa benda", "massa"):
        try:
            energi_kinetik = int(input("\n..Besar energi kinetik (Joule)\t: "))
            kecepatan = int(input("..Kecepatan dari sebuah benda\t: "))
        except ValueError:
            return kinetik()
        massa = energi_kinetik / 0.5 / (pow(kecepatan, 2))
        caraKinetik()
    elif nilai in ("kecepatan benda", "kecepatan", "cepat benda", "cepat"):
        try:
            energi_kinetik = int(input("\n..Besar energi kinetik (Joule)\t: "))
            massa = int(input("..Massa dari sebuah benda\t: "))
        except ValueError:
            return kinetik()
        kecepatan = math.sqrt(energi_kinetik / 0.5 / massa)
        caraKinetik()
    else:
        kinetik()

def potensial():
    global energi_potensial, massa, tinggi, gravitasi, nilai
    os.system("cls")
    menu.REP()
    nilai = input("Tulis disini : ").lower()
    if nilai in ("energi potensial", "potensial"):  
        try:
            massa = int(input("\n..Massa benda (kg)\t\t  : "))
            gravitasi = int(input("..Percepatan gravitasi bumi\t  : "))
            tinggi = int(input("..Ketinggian benda dari tanah (m) : "))
        except ValueError:
            return potensial()
        energi_potensial = massa * gravitasi * tinggi
        caraPotensial()
    elif nilai in ("massa benda", "massa"):
        try:
            energi_potensial = int(input("\n..Besar energi potensial (Joule)  : "))
            gravitasi = int(input("..Percepatan gravitasi bumi\t  : "))
            tinggi = int(input("..Ketinggian benda dari tanah (m) : "))
        except ValueError:
            return potensial()
        massa = energi_potensial / (gravitasi * tinggi)
        caraPotensial()
    elif nilai in ("ketinggian benda", "ketinggian", "tinggi benda", "tinggi"):
        try:
            energi_potensial = int(input("\n..Besar energi potensial (Joule) : "))
            massa = int(input("..Massa dari sebuah benda\t : "))
            gravitasi = int(input("..Percepatan gravitasi bumi\t : "))
        except ValueError:
            return potensial()
        tinggi = energi_potensial / (massa * gravitasi)
        caraPotensial()
    else:
        potensial()

def caraKinetik():
    if nilai in ("energi kinetik", "kinetik"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Massa benda adalah {massa} kg
                   Kecepatan sebuah benda adalah {kecepatan} m/s

        Ditanya  : Energi Kinetik Benda ?

        Jawab    : EK = 1/2 x m x v^2
                   EK = 1/2 x {massa} x {kecepatan}^2
                   EK = {0.5 * massa} x {pow(kecepatan, 2)}
                   EK = {energi_kinetik}
        Jadi, energi kinetik yang dihasilkan dari benda tersebut adalah {energi_kinetik} Joule""")
        
    elif nilai in ("massa benda", "massa"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Energi kinetik suatu benda adalah {energi_kinetik} Joule
                   Kecepatan sebuah benda adalah {kecepatan} m/s

        Ditanya  : Massa Benda ?

        Jawab    : Massa = EK : 1/2 x v^2
                   Massa = {energi_kinetik} : 1/2 x {kecepatan}^2
                   Massa = {energi_kinetik} : {(0.5 * (pow(kecepatan, 2)))}
                   Massa = {massa}
        Jadi, massa dari sebuah benda tersebut adalah {massa} Kg""")

    elif nilai in ("kecepatan benda", "kecepatan", "cepat benda", "cepat"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Energi kinetik suatu benda adalah {energi_kinetik} kg
                   Massa sebuah benda adalah {massa} m/s

        Ditanya  : Kecepatan Benda ?

        Jawab    : Kecepatan^2 = EK : 1/2 x massa
                   Kecepatan^2 = {energi_kinetik} : 1/2 x {massa}^2
                   Kecepatan^2 = {energi_kinetik} : {0.5 * massa}
                   Kecepatan^2 = {energi_kinetik / 0.5 / massa}
                   Kecepatan   = {kecepatan}
        Jadi, kecepatan dari sebuah benda tersebut adalah {kecepatan} Kg""")

def caraPotensial():
    if nilai in ("energi potensial", "potensial"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Massa benda adalah {massa} kg
                   Percepatan gravitasi bumi adalah {gravitasi} m/s2
                   Ketinggian suatu benda dari tanah {tinggi} m
                   
        Ditanya  : Energi Potensial Benda ?

        Jawab    : EP = m x g x h
                   EP = {massa} x {gravitasi} x {tinggi}
                   EP = {massa * gravitasi} x {tinggi}
                   EP = {energi_potensial}
        Jadi, energi potensial yang dihasilkan dari benda tersebut adalah {energi_potensial} Joule""")

    elif nilai in ("massa benda", "massa"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Energi potensial benda adalah {energi_potensial} Joule
                   Percepatan gravitasi bumi adalah {gravitasi} m/s2
                   Ketinggian suatu benda dari tanah {tinggi} m

        Ditanya  : Massa Benda ?

        Jawab    : Massa = EP : g x h
                   Massa = {energi_potensial} : {gravitasi} x {tinggi}
                   Massa = {energi_potensial} : {gravitasi * tinggi}
                   Massa = {massa}
        Jadi, massa benda dari benda tersebut adalah {massa} Kg""")

    elif nilai in ("ketinggian benda", "ketinggian", "tinggi benda", "tinggi"):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui: Energi potensial benda adalah {energi_potensial} Joule
                   Percepatan gravitasi bumi adalah {gravitasi} m/s2
                   Massa suatu benda adalah {massa} kg

        Ditanya  : Ketinggian benda ?

        Jawab    : Tinggi Benda = EP : m x h
                   Tinggi Benda = {energi_potensial} : {massa} x {gravitasi}
                   Tinggi Benda = {energi_potensial} : {massa * gravitasi}
                   Tinggi Benda = {tinggi}
        Jadi, ketinggian benda dari tanah adalah {massa} m""")

def suara(path):
    with open(path, "r") as f:
        teks = f.read()
        print("\n"+teks)
        isi = teks.replace("\n", " ")
        output = gTTS(text=isi, lang="id", slow=False)
        try:
            output.save("suara.mp3")
            playsound("suara.mp3", True)
            os.remove("suara.mp3")
        except gTTSError:
            print("""
-------------------------------------------------------------------
---------- PASTIKAN PERANGKAT KAMU TERHUBUNG KE INTERNET ----------
     ---------- UNTUK BISA MENDENGARKAN FITUR SUARA ----------
-------------------------------------------------------------------
            """)

def kimia(mencari):
    
    if mencari == "unsur":
        path = r"C:\Users\SYITA\Documents\PROGRAM\Final project\final\Database\unsur opsi 2.txt"
        suara(path)
    elif mencari == "senyawa":
        path = r"C:\Users\SYITA\Documents\PROGRAM\Final project\final\Database\senyawa opsi 2.txt"
        suara(path)
    elif mencari == "campuran":
        path = r"C:\Users\SYITA\Documents\PROGRAM\Final project\final\Database\campuran opsi 2.txt"
        suara(path)
    else:
        print("\n..... MAAF, KATA KUNCI TIDAK TERDAFTAR .....")