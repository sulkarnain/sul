# Nama file: imfortmath.py

#mengimpor modul math2
import math2

def main():
    # balok
    p = 12    # panjang
    l = 6     # lebar
    
    luas = math2.luasBalok(p * l, p * t, l * t)
    kel  = math2.kelilingBalok(p, l, t)

    print("BALOK")
    print("Panjang\t:", p)
    print("lebar\t:", l)
    print("Tinggi\t:", t)
    print("Luas\t:", luas)
    print("Keliling\t:", kel)

    #jajar genjang
    jarijari = 4

    luas = math2.luasJajarGenjang(jarijari)
    kel  = math2.kelilingJajarGenjang(jarijari)

    print("\nJAJARGENJANG")
    print("jarijari\t:", jarijari)
    
    print("Luas\t:", luas)
    print("Keliling\t:", kel)

if __name__ == "__main__":
    main()
