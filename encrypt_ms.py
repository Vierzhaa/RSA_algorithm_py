import math, json, os, time, platform
FILE_NAME="Rsa_ms.json"

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
def crel_prima(n):
    relatif_prima = []
    
    for e in range(2, n):
        if math.gcd(e, n) == 1:
            relatif_prima.append(e)
    return relatif_prima
def desimal_ke_biner(n):
    if n == 0:
        return "0"
    hasil = ""
    while n > 0:
        hasil = str(n % 2) + hasil
        n //= 2
    return hasil
def encryptt(m):
    o=[]
    c=[]
    charw=list(m)
    for i in range(len(charw)):
        o.append(ord(charw[i]))
    for k in range(len(o)):
        c.append(pow(o[k],e,n))
    pbin=[desimal_ke_biner(v) for v in c]
    return pbin
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
c()
while True:
    lm=load()
    printt("hai hai hai, pilih ya")
    print("\n1. encrypt pesan\n2. lihat pesan\n3. hapus pesan\n4. keluar")
    option=input("opsi : ")
    c()
    if option == "1":
        m=input("apa pesan kamu (enter untuk cancel) : ")
        if m == "":
            back()
            continue
        em=encryptt(m)
        new_id =lm[-1]['id'] + 1 if lm else 1
        lm.append({"id" : new_id, "pesan" : em })
        save(lm)
        print("sukses")
        back()
    elif option == "2":
        printt("=== Your message ===\n")
        if not lm:
            printt("ga ada\n")
            back()
        else:
            for t in lm:
                print(f"{t['id']}. {" ".join(t['pesan'])}")
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