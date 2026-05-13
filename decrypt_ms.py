import math, json, time, os, platform
FILE_NAME="Rsa_ms.json"

def crel_prima(n):
    relatif_prima = []
    
    for e in range(2, n):
        if math.gcd(e, n) == 1:
            relatif_prima.append(e)
    return relatif_prima
def c():
        system_name = platform.system().lower()
        if "windows" in system_name:
            os.system("cls")
        elif "linux" in system_name or "darwin" in system_name:
            os.system("clear")
def printt(a):
    for c in a:
        print(c, end="", flush=True)
        time.sleep(0.05)
    print("")
def biner_ke_desimal(b):
        hasil = 0
        for i, bit in enumerate(reversed(b)):
            hasil += int(bit) * (2 ** i)
        return hasil
def decryptt(c):
    uc=[biner_ke_desimal(v) for v in c]
    op=[pow(j,d,n) for j in uc]
    um=[chr(b) for b in op]
    return "".join(um)
def private_key(e,phi_n):
    return pow(e,-1,phi_n)
def load():
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
def save(m):
        with open(FILE_NAME, 'w') as file:
            json.dump(m, file, indent=4)
def back():
    input("back : ")
    c()

p=11
q=13
n=p*q#aman
phi_n=(p-1)*(q-1)
le=crel_prima(phi_n)
e=le[0] #aman public key
d=private_key(e,phi_n)#private key
c()
while True:
    lm=load()
    printt("hai hai hai, pilih ya")
    print("1. decrypt pesan\n2. lihat pesan\n3. hapus pesan\n4. keluar")
    option=input("opsi : ")
    c()
    if option=="1":      
        if not lm:
            print("=== Your message ===\n")   
            print("ga ada")
            back()
        else:     
            ketemu=False      
            while not ketemu:
                print("=== Your message ===\n")
                for t in lm:
                    print(f"{t['id']}. {" ".join(t['pesan'])}")
                try: 
                    op=int(input("mau decrypt yang mana : "))
                    for i in lm:
                        if op == i['id']:
                            print(f"pesannya : {decryptt(i['pesan'])}")
                            ketemu=True
                    if ketemu:
                        back()
                        break
                    elif not ketemu:
                        print("ID tidak ada")
                        back()
                        break
                except ValueError:
                    print("harus angka")
                    back()
            
    elif option == "2":
        if lm:
            print("=== Your message ===\n")
            for t in lm:
                print(f"{t['id']}. {" ".join(t['pesan'])}")
            back()
        else:
            print("=== Your message ===\n")
            print("ga ada")
            back()
    elif option == '3':
        while True:
            print("=== Your message ===\n")
            for t in lm:
                print(f"{t['id']}. {" ".join(t['pesan'])}")
            try:
                id_hapus = int(input("Masukkan ID pesan yang ingin dihapus (0 untuk calcel) ): "))
                if id_hapus == 0:
                    back()
                    break
                daftar_baru = [t for t in lm if t['id'] != id_hapus]
                if len(daftar_baru) < len(lm):
                    save(daftar_baru)
                    print(f"pesan {id_hapus} berhasil dihapus.")
                    back()
                    break
                else:
                    print("ID tidak ditemukan.")
                    back()
            except ValueError:
                print("Masukkan ID berupa angka.")
                back()
    elif option == "4":
        printt("bye bye")
        break
    else:
        printt("you yang bener dong")
        back()

#13/05/26 11:39