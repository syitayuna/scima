import menu
import math
import os

def inputBarisan():
    os.system("cls")
    menu.suku_ke()
    global a, b
    try:
        a = int(input("Masukkan nilai suku pertama : "))
        b = int(input("Masukkan nilai beda         : "))
    except ValueError:
        inputBarisan()

def inputDeret():
    os.system("cls")
    menu.jumlah_suku_ke()
    global a, b
    try:
        a = int(input("Masukkan nilai suku pertama : "))
        b = int(input("Masukkan nilai beda         : "))
    except ValueError:
        inputDeret()

def barisan(cari):
    inputBarisan()
    print()
    print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
    print(60 * "=")
    print(f"""
    Diketahui : Suku pertama : {a}
                Beda         : {b}

    Ditanya   : Suku ke {cari[2]}

    Jawab     : U{cari[2]} = a + (n-1) b
                U{cari[2]} = {a} + ({cari[2]}-1) x {b}
                U{cari[2]} = {a} + {int(cari[2]) - 1} x {b}
                U{cari[2]} = {a + ((int(cari[2]) - 1) * b)}""")

def deret(cari):
    inputDeret()
    print()
    print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
    print(60 * "=")
    print(f"""
    Diketahui : Suku pertama : {a}
                Beda         : {b}

    Ditanya   : Jumlah {cari[1]} suku pertama

    Jawab     : S{cari[1]} = n/2 [2a + (n-1) b]
                S{cari[1]} = {cari[1]}/2 [2{a} + ({cari[1]}-1) {b}]
                S{cari[1]} = {int(cari[1])/2} [{2*a} + {int(cari[1])-1} x {b}]
                S{cari[1]} = {(int(cari[1])/2)*((2*a)+(int(cari[1])-1)*b)}""")

class Teorema:

    def __init__(self, diket_1, diket_2, dita, operator, rumus):
        self.diket_1 = diket_1
        self.diket_2 = diket_2
        self.dita = dita
        self.oper = operator
        self.cara = rumus

    def miring(self, objek):
        os.system("cls")
        menu.rumteo()
        print(60 * '-')
        print("      Mencari : Panjang Sisi Miring Segitiga Siku Siku")
        print(60 * '-')
        try:
            self.sisi_1 = int(input("Panjang sisi tegak\t : "))
            self.sisi_2 = int(input("Panjang sisi alas\t : "))
            self.satpan = input("Satuan panjang segitiga\t : ")
        except ValueError:
            return self.miring(self)
        self.akar = pow(self.sisi_1, 2) + pow(self.sisi_2, 2)
        self.hasil = math.sqrt(pow(self.sisi_1, 2) + pow(self.sisi_2, 2))
        objek.proses(self)

    def tegak(self, objek):
        os.system("cls")
        menu.rumteo()
        print(60 * '-')
        print("      Mencari : Panjang Sisi Tegak Segitiga Siku Siku")
        print(60 * '-')
        try:
            self.sisi_1 = int(input("Panjang sisi miring\t : "))
            self.sisi_2 = int(input("Panjang sisi alas\t : "))
            self.satpan = input("Satuan panjang segitiga\t : ")
        except ValueError:
            return self.tegak(self)
        self.akar = pow(self.sisi_1, 2) - pow(self.sisi_2, 2)
        self.hasil = math.sqrt(pow(self.sisi_1, 2) - pow(self.sisi_2, 2))
        objek.proses(self)

    def alas(self, objek):
        os.system("cls")
        menu.rumteo()
        print(60 * '-')
        print("      Mencari : Panjang Sisi Alas Segitiga Siku Siku")
        print(60 * '-')
        try:
            self.sisi_1 = int(input("Panjang sisi miring\t : "))
            self.sisi_2 = int(input("Panjang sisi tegak\t : "))
            self.satpan = input("Satuan panjang segitiga\t : ")
        except ValueError:
            return self.alas(self)
        self.akar = pow(self.sisi_1, 2) - pow(self.sisi_2, 2)
        self.hasil = math.sqrt(pow(self.sisi_1, 2) - pow(self.sisi_2, 2))
        objek.proses(self)

    def proses(self, objek):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui : {objek.diket_1} segitiga siku siku adalah {objek.sisi_1} {objek.satpan}
                    {objek.diket_2} segitiga siku siku adalah {objek.sisi_2} {objek.satpan}

        Ditanya   : Panjang {objek.dita} ?

        Jawab     : {objek.dita} = {objek.cara}
                    {objek.dita} = akar {objek.sisi_1}^2 {objek.oper} {objek.sisi_2}^2
                    {objek.dita} = akar {pow(objek.sisi_1, 2)} {objek.oper} {pow(objek.sisi_2,2)}
                    {objek.dita} = akar {objek.akar}
                    {objek.dita} = {objek.hasil}
        Jadi, panjang {objek.dita} segitiga siku siku adalah {objek.hasil} {objek.satpan}""")

class Kubus:

    def __init__(self, dita, rumus):
        self.dita = dita
        self.rumus = rumus

    def volume(self, objek):
        os.system("cls")
        menu.rumus_volume_kubus()
        print('-'*60)
        try:
            self.sisi = int(input("Panjang sisi kubus : "))
        except ValueError:
            return self.volume(self)
        self.var = f"{self.sisi}^3"
        self.hasil = pow(self.sisi, 3)
        objek.cara(self)
        
    def luas(self, objek):
        os.system("cls")
        menu.rumus_luas_kubus()
        print('-'*60)
        try:
            self.sisi = int(input("Panjang sisi kubus : "))
        except ValueError:
            return self.luas(self)
        self.var = f"6 x {self.sisi}^2"
        self.hasil = 6 * pow(self.sisi, 2)
        objek.cara(self)
        
    def cara(self, objek):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui : Panjang sisi kubus : {objek.sisi}

        Ditanya   : {objek.dita} ?
        
        Jawab     : {objek.dita} = {objek.rumus}
                    {objek.dita} = {objek.var}
                    {objek.dita} = {objek.hasil}
        """)

class Balok:

    def __init__(self, dita, rumus):
        self.dita = dita
        self.rumus = rumus

    def volume(self, objek):
        os.system("cls")
        menu.rumus_volume_balok()
        print('-'*60)
        try:
            self.panjang = int(input("Panjang balok : "))
            self.lebar = int(input("Lebar balok   : "))
            self.tinggi = int(input("Tinggi balok  : "))
        except ValueError:
            return self.volume(self)
        self.var = f"{self.panjang} x {self.lebar} x {self.tinggi}"
        self.hasil = self.panjang * self.lebar * self.tinggi
        objek.cara(self)

    def luas(self, objek):
        os.system("cls")
        menu.rumus_luas_balok()
        print('-'*60)
        try:
            self.panjang = int(input("Panjang balok : "))
            self.lebar = int(input("Lebar balok   : "))
            self.tinggi = int(input("tinggi balok  : "))
        except ValueError:
            return self.luas(self)
        self.var = f"2 x (({self.panjang} x {self.lebar}) + ({self.panjang} x {self.tinggi}) + ({self.lebar} x {self.tinggi}))"
        self.hasil = 2 * ((self.panjang*self.lebar) + (self.panjang*self.tinggi) + (self.lebar*self.tinggi))
        objek.cara(self)

    def cara(self, objek):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui : Panjang Balok = {objek.panjang}
                    Lebar Balok   = {objek.lebar}
                    Tinggi Balok  = {objek.tinggi}

        Ditanya   : {objek.dita} ?

        Jawab     : {objek.dita}  = {objek.rumus}
                    {objek.dita}  = {objek.var}
                    {objek.dita}  = {objek.hasil}
                    """)

class Bola:

    def __init__(self, dita, rumus):
        self.dita = dita
        self.rumus = rumus

    def volume(self, objek):
        os.system("cls")
        menu.rumus_volume_bola()
        print('-'*60)
        try:
            self.jari = int(input("Panjang jari jari : "))
        except ValueError:
            return self.volume(self)
        self.var = f"4/3 x {math.pi:.2f} x {self.jari**3}"
        self.hasil = 4/3 * math.pi * pow(self.jari, 3)
        objek.cara(self)

    def luas(self, objek):
        os.system("cls")
        menu.rumus_luas_bola()
        print('-'*60)
        try:
            self.jari = int(input("Panjang jari jari bola : "))
        except ValueError:
            return self.luas(self)
        self.var = f"4 x {math.pi:.2f} x {self.jari**2}"
        self.hasil = 4 * math.pi * pow(self.jari, 2)
        objek.cara(self)

    def cara(self, objek):
        print("")
        print("SILAHKAN SIMAK PENJELASAN CARANYA".center(60, "-"))
        print(60 * "=")
        print(f"""
        Diketahui : Panjang Jari Jari Lingkaran = {objek.jari}

        Ditanya   : {objek.dita} ?

        Jawab     : {objek.dita}  = {objek.rumus}
                    {objek.dita}  = {objek.var}
                    {objek.dita}  = {objek.hasil:.2f}
                    """)

# INSTANCE KELAS BANGUN KUBUS
volume_kubus = Kubus("Volume Kubus", "sisi^3")
luas_kubus = Kubus("Luas Kubus", "6 x sisi^2")
cara_kubus =Kubus(None, None)

# INSTANCE KELAS BANGUN BALOK
volume_balok = Balok("Volume Balok", "Panjang x Lebar x Tinggi")
luas_balok = Balok("Luas Balok", "2 x ((P x L) + (P x T) + (L x T))")
cara_balok = Balok(None, None)

# INSTANCE KELAS BANGUN BOLA
volume_bola = Bola("Volume Bola", "4/3 x pi x jari-jari^3")
luas_bola = Bola("Luas Bola", "4 x pi x jari-jari^2")
cara_bola = Bola(None, None)

# INSTANCE KELAS TEOREMA PYTHAGORAS
sisi_miring = Teorema("Sisi tegak", "Sisi alas", "Sisi miring", "+", "akar b^2 + c^2")
sisi_tegak = Teorema("Sisi miring", "Sisi alas", "Sisi tegak", '-', "akar a^2 - c^2")
sisi_alas = Teorema("Sisi miring", "Sisi tegak", "Sisi alas", '-', "akar a^2 - b^2")
cara_teorema = Teorema(None, None, None, None, None,)