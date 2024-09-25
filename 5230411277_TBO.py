def volume(r, t):
    return 1/3*3.14*r*r*t

def LuasSelimut(r, s):
    return 3.14*r*s

def LuasAlas(r):
    return 3.14*r*r


def main():
    print("=====Menu Perhitungan Kerucut=====")
    print("1. Menghitung Volume")
    print("2. Menghitung Luas Selimut")
    print("3. Menghitung Luas Alas")
    print("4. Keluar")
    while True:
        pilihMenu = input("Pilih Menu di atas: ")
        if pilihMenu == "1":
            r = int(input("Masukan jari-jari kerucut: "))
            t = int(input("Masukan tinggi kerucut: "))
            hasil = volume(r, t)
            print(hasil)
            
        elif pilihMenu == "2":
            r = int(input("Masukan jari jari kerucut: "))
            s = int(input("Masukan panjang sisi kerucut: "))
            hasil = LuasSelimut(r, s)
            print(hasil)

        elif pilihMenu == "3":
            r = int(input("Masukan jari-jari kerucut: "))
            hasil = LuasAlas(r)
            print(hasil)

        elif pilihMenu == "4":
            print("Anda keluar dari program, Terima Kasih :) ")
            break
        else:
            print("Menu yang anda pilih tidak ada")
    
if __name__ == "__main__":
    main()





