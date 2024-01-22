def main():
    print("""
            =============================
      ----- SELAMAT DATANG, SELAMAT BELAJAR -----
            =============================

...DALAM PROGRAM INI KAMI MENYEDIAKAN 2 TEMA :
--------------------------------------------------
    1. MATEMATIKA
    2. SAINS FISIKA
--------------------------------------------------

Silahkan untuk memilih tema yang anda inginkan ...""")

def math():
    print("\n...ANDA MEMILIH TEMA MATEMATIKA DALAM PROGRAM INI")
    print("""DISINI TERSEDIA : 
            1. TEOREMA PYTHAGORAS 
            2. BANGUN RUANG 3 DIMENSI  
            3. BARISAN DAN DERET ARITMATIKA 
            
            00. Kembali""")

def sains():
    print("\n...ANDA MEMILIH TEMA SAINS FISIKA DALAM PROGRAM INI")
    print("""DISINI TERSEDIA :
            1. ENERGI KINETIK   
            2. ENERGI POTENSIAL   
            3. MATERI UNSUR, SENYAWA, DAN CAMPURAN  
            
            00. Kembali""")

def REK():
    print("")
    print("------------------".center(60))
    print("   ENERGI KINETIK   ".center(60, "-"))
    print("------------------".center(60))
    print("\n  UNTUK MENGHITUNG ENERGI KINETIK, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    EK = 1/2 x m x v^2

    DENGAN
    EK = Energi Kinetik (J)
    m  = massa benda (kg)
    v  = kecepatan benda (m/s)\n""")
    print("...Dalam materi energi kinetik, ingin mencari nilai apa ?")

def REP():
    print("")
    print("------------------".center(60))
    print("   ENERGI POTENSIAL   ".center(60, "-"))
    print("------------------".center(60))
    print("\n  UNTUK MENGHITUNG ENERGI POTENSIAL, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    EP = m x g x h

    DENGAN
    EP = Energi Potensial (J)
    m  = massa benda (kg)
    g  = percepatan gravitasi bumi (10 m/s^2)
    h  = ketinggian benda dari tanah (m)\n""")
    print("...Dalam materi energi potensial, ingin mencari nilai apa ?")

def rumteo():
    print("""
            TEOREMA PYTHAGORAS
            ------------------
    Bisa dihitung dengan menggunakan Rumus :
                   ------
    a^2 = b^2 + c^2   =>   a = akar b^2 + c^2
    b^2 = a^2 - c^2   =>   b = akar a^2 - c^2
    c^2 = a^2 - b^2   =>   c = akar a^2 - b^2

                C
                |\ 
                | \ 
                |  \ 
                |   \ 
             b  |    \  a
                |     \ 
                |      \ 
                |_______\ 
                A   c    B


            a = sisi miring
            b = sisi tegak
            c = sisi alas\n""")
    print("...Dalam materi Teorema Pythagoras, ingin mencari nilai apa ?")

def menu_ruang():
    print("""
    DI PROGRAM INI BISA MENGHITUNG :
    1. LUAS DAN VOLUME BANGUN KUBUS
    2. LUAS DAN VOLUME BANGUN BALOK
    3. LUAS DAN VOLUME BANGUN BOLA
    NOTE :
    TULISKAN KATA KUNCI DENGAN FORMAT "MENCARI (NILAI YANG ANDA CARI) (NAMA BANGUN) !
    CONTOH : "MENCARI LUAS BOLA"
    """)

def aritmatika():
    print("""
    DI PROGRAM INI BISA MENGHITUNG :
    1. SUKU KE N BARISAN ARITMATIKA
    2. JUMLAH N SUKU PERTAMA
    NOTE :
    TULISKAN KATA KUNCI DENGAN FORMAT DIATAS MINIMAL 3 KATA !
    CONTOH: "SUKU KE 21" ATAU "JUMLAH 20 SUKU"
    """)


def rumus_volume_kubus():
    print("")
    print("------------------".center(60))
    print("   VOLUME KUBUS   ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG VOLUME KUBUS, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    VK = s x s x s
    
    DENGAN
    VK = Volume Kubus 
    s  = sisi\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung volume kubus")

def rumus_luas_kubus():
    print("")
    print("------------------".center(60))
    print("    LUAS KUBUS    ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG LUAS KUBUS, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    LK = 6 x s^2
    
    DENGAN 
    LK = Luas Kubus
    s  = sisi\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung luas kubus")

def rumus_volume_balok():
    print("")
    print("------------------".center(60))
    print("   VOLUME BALOK   ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG VOLUME BALOK, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    VB = p x l x t

    DENGAN 
    VB = Volume Balok
    p  = panjang
    l  = lebar 
    t  = tinggi\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung volume balok")

def rumus_luas_balok():
    print("")
    print("------------------".center(60))
    print("    LUAS BALOK    ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG LUAS BALOK, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    LB = 2 ((p x l) + (p x t) + (l x t))

    DENGAN
    LB = Luas Balok
    p  = panjang
    l  = lebar 
    t  = tinggi\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung luas balok")

def rumus_volume_bola():
    print("")
    print("------------------".center(60))
    print("    VOLUME BOLA    ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG VOLUME BOLA, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    VB = 4/3 x phi x r^3
    
    DENGAN
    VB    = Volume Bola
    phi   = 3,14
    r     = jari - jari\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung volume bola")

def rumus_luas_bola():
    print("")
    print("------------------".center(60))
    print("     LUAS BOLA    ".center(60, '-'))
    print("------------------".center(60))
    print("\n     UNTUK MENGHITUNG LUAS BOLA, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    LB= 4 x phi x r^2 

    DENGAN 
    LB    = Luas Bola
    phi   = 3,14
    r     = jari - jari\n""")
    print("...Inputkan nilai yang diperlukan dalam mencari luas bola")

def suku_ke():
    print("")
    print("------------------".center(60))
    print("     SUKU KE-N    ".center(60, '-'))
    print("------------------".center(60))
    print("\n  UNTUK MENGHITUNG SUKU KE-N, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    UN = a + (n-1) b

    DENGAN 
    UN  = Suku ke-N
    a   = suku awal 
    b   = beda\n""")
    print("...Inputkan nilai yang diperlukan dalam mencari suku ke-n ")

def jumlah_suku_ke():
    print("")
    print("------------------".center(60))
    print("   JUMLAH SUKU N   ".center(60, '-'))
    print("------------------".center(60))
    print("\n  UNTUK MENGHITUNG SUKU KE-N, BISA MENGGUNAKAN RUMUS")
    print(60 * "=")
    print("""
    SN = n/2 (a+U_n)

    DENGAN
    SN  = Jumlah Suku ke-N
    a   = suku awal 
    b   = beda\n""")
    print("...Inputkan nilai yang diperlukan dalam menghitung jumlah suku ke-n")

def kimia():
    print("""
    .....INI MERUPAKAN MATERI KIMIA.....
    -------------------------------------
    DI PRORAM INI TERDAPAT MATERI :
    1. UNSUR
    2. SENYAWA
    3. CAMPURAN

    NOTE :
    TULISKAN KATA KUNCI MATERI APA YANG ANDA CARI !
    CONTOH: "UNSUR" 
    """)