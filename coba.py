def REK():
    print("")
    print("")

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
    elif nilai in ("massa Benda", "massa"):
        try:
            energi_kinetik = int(input("\n..Besar energi kinetik (Joule)\t: "))
            kecepatan = int(input("..Kecepatan dari sebuah benda\t: "))
        except ValueError:
            return kinetik()
        massa = energi_kinetik / 0.5 / (pow(kecepatan, 2))
        caraKinetik()
    elif nilai in ("kecepatan benda", "kecepatan", "cepat Benda", "cepat"):
        try:
            energi_kinetik = int(input("\n..Besar energi kinetik (Joule)\t: "))
            massa = int(input("..Massa dari sebuah benda\t: "))
        except ValueError:
            return kinetik()
        kecepatan = math.sqrt(energi_kinetik / 0.5 / massa)
        caraKinetik()
    else:
        kinetik()