import csv
import pwinput
from prettytable import PrettyTable
table = PrettyTable()
table2 = PrettyTable()

def refresh_table_film():
    table.clear() #menghapus array dalam baris
    table.title = "DAFTAR FILM REGULER" #judul table. paling atas
    table.field_names = ["No", "Film", "Harga", "Status"] #field table kamar ketika jadi pengunjung
    for film in daftar_film:
            if film["status"] == "On Showing": 
                table.add_row([film["nomor"], film["film"], film["harga"], film["status"]])
    
    table2.clear() #menghapus array dalam baris
    table2.title = "DAFTAR FILM PREMIER " #judul table2. paling atas
    table2.field_names = ["No", "Film", "Harga", "Status"] #field table2 kamar ketika jadi pengunjung
    for film in daftar_film_premier:
            if film["status"] == "On Showing": 
                table2.add_row([film["nomor"], film["film"], film["harga"], film["status"]])

#--------Membuat CSV----------
def load_data():
    global userpass, data_user, daftar_film, daftar_film_premier, voucher
    userpass = []
    try:
        with open("userpass.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                userpass.append({"username": row[0], "password": row[1]})
    except FileNotFoundError:
        open("userpass.csv", 'w', newline='')

    data_user = []
    try:
        with open("data_user.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_user.append({"username": row[0], "member": row[1], "kode member" : row[2], "saldo": int(row[3]), "e-pay": int(row[4])})
    except FileNotFoundError:
        open("data_user.csv", 'w', newline='')

    try:
        daftar_film = []
        with open("daftar_film.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                daftar_film.append({"nomor": row[0], "film": row[1], "harga": int(row[2]), "status": row[3]})
    except FileNotFoundError:

        daftar_film = [
            {"nomor": "01", "film": "Dusun pocong", "harga": 50000, "status": "On Showing"},
            {"nomor": "02", "film": "Kultus iblis", "harga": 40000, "status": "On Showing"},
            {"nomor": "03", "film": "Saranjana", "harga": 60000, "status": "On Showing"},
            {"nomor": "04", "film": "Exorcis", "harga": 60000, "status": "On Showing"}
        ]
        with open("daftar_film.csv", 'w', newline='') as file:
            fieldnames = ["nomor", "film", "harga", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for film in daftar_film:
                writer.writerow(film) #writerow untuk mengambil 1 baris. writerows mengambil lebih dari satu baris.

    try:
        daftar_film_premier = []
        with open("daftar_film_premier.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                daftar_film_premier.append({"nomor": row[0], "film": row[1], "harga": int(row[2]), "status": row[3]})
    except FileNotFoundError:

        daftar_film_premier = [
            {"nomor": "01", "film": "Dusun pocongg", "harga": 150000, "status": "On Showing"},
            {"nomor": "02", "film": "Kultus iblis", "harga": 140000, "status": "On Showing"},
            {"nomor": "03", "film": "Saranjana", "harga": 160000, "status": "On Showing"},
            {"nomor": "04", "film": "Exorcis", "harga": 160000, "status": "On Showing"}
        ]
        with open("daftar_film_premier.csv", 'w', newline='') as file:
            fieldnames = ["nomor", "film", "harga", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for film in daftar_film_premier:
                writer.writerow(film) #writerow untuk mengambil 1 baris. writerows mengambil lebih dari satu baris.

    voucher = []
    try:
        with open("voucher.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                voucher.append({"kode": row[0], "nama_voucher": row[1], "persen": int(row[2]), "status": row[3]})
    except FileNotFoundError:
        open("voucher.csv", 'w', newline='')

        voucher = [
            {"kode": "A45678B", "nama_voucher": "Promo 50%", "persen": 50, "status": "belum digunakan"},
            {"kode": "A12345B", "nama_voucher": "Promo 40%", "persen": 40, "status": "belum digunakan"},
            {"kode": "A67890B", "nama_voucher": "Promo 30%", "persen": 30, "status": "belum digunakan"},
            {"kode": "A34567B", "nama_voucher": "Promo 20%", "persen": 20, "status": "belum digunakan"}
        ]
        with open("voucher.csv", 'w', newline='') as file:
            fieldnames = ["kode", "nama_voucher", "persen", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for kode in voucher:
                writer.writerow(kode) #writerow untuk mengambil 1 baris. writerows mengambil lebih dari satu baris.


load_data()

#--------Simpan Data----------
def simpan_data():
    with open("userpass.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for akun in userpass:
            writer.writerow([akun["username"], akun["password"]])
    
    with open("data_user.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for user in data_user:
            writer.writerow([user["username"], user["member"], user["kode member"], user["saldo"], user["e-pay"]])

    with open("daftar_film.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for film in daftar_film:
            writer.writerow([film["nomor"], film["film"], film["harga"], film["status"]])
    
    with open("daftar_film_premier.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for film in daftar_film_premier:
            writer.writerow([film["nomor"], film["film"], film["harga"], film["status"]])

    with open("voucher.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for kode in voucher:
            writer.writerow([kode["kode"], kode["nama_voucher"], kode["persen"], kode["status"]])

simpan_data()
load_data()

#--------Input Handler--------

def inputhandler(prompt, inputtype="str"):
    while True:
        try:
            if inputtype == "str":
                userinput = input(prompt)
            elif inputtype == "int":
                userinput = int(input(prompt))
            elif inputtype == "digit":
                userinput = input(prompt)
                if not userinput.isdigit():
                    print("Input hanya bisa berupa angka\n")
                    return inputhandler(prompt, "digit") #Return itu digunakan untuk mengembalikan value ke fungsi
            return userinput
        except KeyboardInterrupt:
            print("\nGabisa Error!\n")
        except ValueError:
            print("Input hanya bisa berupa angka\n")
        except Exception as error:
            print(f"Error baru nih: {error}\n")

#------Membuat Akun User----------
def login_user():
    print("\n-----------------LOGIN-----------------")
    username = inputhandler("Username: ")
    password = pwinput.pwinput("Password: ", mask='*')

    sukses = False
    for akun in userpass:
        if akun["username"] == username and akun["password"] == password:
            sukses = True
            
    for user in data_user:
        if user["username"] == username:
            global current_user
            current_user = user 

    if(sukses):
        print("Login Berhasil!")
        refresh_table_film()
        menu()
    else:
        print('Gagal Login!')

def register_user():
    print("\n---------------BUAT AKUN---------------")
    while True:
        username = inputhandler("Username: ").strip()
        if len(username) < 5:
            print("Minimal 5 huruf")
        else:
            break
    while True:
        try:
            password = pwinput.pwinput("Password: ", mask='*').strip()
            if len(password) < 5:
                print("Minimal 5 huruf")
            else:
                break
        except KeyboardInterrupt:
            print("Hayolo!")

    sudah_ada = False
    for akun in userpass:
        if akun["username"] == username:
            sudah_ada = True
    
    if sudah_ada:
        print("Username sudah ada")
    else:
        data_user.append({"username": username, "member": "biasa", "kode member": "", "saldo": 0, "e-pay": 0})
        simpan_data()

        userpass.append({"username": username, "password": password})
        with open('userpass.csv', 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([username, password])

        global user_type, current_user
        user_type = "normal"
        current_user = data_user[-1]
        
        print("\nAkun berhasil dibuat")
        login_user()
        refresh_table_film()

def relog():
    while True:
        tanya = str(input("\n*Apakah anda sudah memiliki akun? y/n: "))
        
        if tanya.lower() == "y":
            login_user()
            print()
            
            
        elif tanya.lower() == "n":
            register_user()
            print()
            login_user()
            break

#---------Format Uang--------
def format_uang(nominal):
    return f"Rp{nominal:,}".replace(',','.')

#------------Proses Menu-------------
def reguler():
    print(table)
    print()
    print(" A1  A2  A3  A4      D6  D7  D8   D9")
    print(" B1  B2  B3  B4      E6  E7  E8   E9")
    print(" C1  C2  C3  C4      F6  F7  F8   F9")
    print("                                    ")
    print("----------------LAYAR---------------")
    print()

    while True:
        nomor = inputhandler("Pilih Film 01/02/03/04: ","digit")
        if len(nomor) < 2:
            print("Minimal 2 huruf")
        elif len(nomor) > 2:
            print("Maksimal 2 huruf")
        else:
            break
    while True:
        duduk = input("Pilih Seat: ")
        if len(duduk) < 2:
            print("Minimal 2 huruf")
        elif len(duduk) > 2:
            print("Maksimal 2 huruf")
        else:
            break
    metode = input("\nPilih metode pembayaran Saldo/E-pay: ")

    for user in data_user:
        if user['member'] == "biasa": 
            isi = input("Apakah memiliki vaucher? y/n: ")
            if isi.lower() == "y":
                isi_lagi = input("Masukkan kode vaucher: ")
                for kode in voucher:
                    if kode["kode"] == isi_lagi:
                        if metode.lower() == "saldo":
                            for film in daftar_film:
                                if film["nomor"] == nomor:
                                    isi = film
                                    nama_film = isi['film']
                                    harga_film = isi['harga']
                                    ket = kode["persen"]
                                    diskon = int(harga_film - (harga_film * (ket / 100)))
                                    saldo = current_user["saldo"]
                                    sisa_duid = current_user["saldo"] - diskon
                                    print("+---------------------------------+")
                                    print("|         INVOICE REGULER!        |")
                                    print("+---------------------------------+")
                                    print(f"Film   : {nama_film}")
                                    print(f"Sheat  : {duduk}")
                                    print(f"Harga  : {format_uang(harga_film)}")
                                    print(f"Diskon : {ket}%")
                                    print(f"Total  : {format_uang(diskon)}")
                                    print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                                    print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                                    print("Terimas Kasih")
                                    kode['status'] = "Digunakan"
                                    current_user["saldo"] = sisa_duid
                                    simpan_data()
                                    refresh_table_film()
                                    return
                            else:
                                print("film tidak ditemukan!")
                        #untuk user biasa di premier menggunakan e-pay
                        elif metode.lower() == "e-pay":
                            for film in daftar_film:
                                if film["nomor"] == nomor:
                                    isi = film
                                    nama_film = isi['film']
                                    harga_film = isi['harga']
                                    ket = kode["persen"]
                                    diskon = int(harga_film - (harga_film * (ket / 100)))
                                    epay = current_user["e-pay"]
                                    sisa_epay = current_user["e-pay"] - diskon
                                    print("+---------------------------------+")
                                    print("|         INVOICE REGULER!        |")
                                    print("+---------------------------------+")
                                    print(f"Film   : {nama_film}")
                                    print(f"Sheat  : {duduk}")
                                    print(f"Harga  : {format_uang(harga_film)}")
                                    print(f"Diskon : {ket}%")
                                    print(f"Total  : {format_uang(diskon)}")
                                    print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                                    print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                                    print("Terimas Kasih")
                                    kode['status'] = "Digunakan"
                                    current_user["e-pay"] = sisa_epay
                                    simpan_data()
                                    refresh_table_film()
                                    return   
                            else:
                                print("film tidak ditemukan!")
                        else:
                            print("Metode pembayaran tidak ditemukan!")
                else:
                    print("Vaucher tidak dapat digunakan!")
            elif isi.lower() == "n":
                if metode.lower() == "saldo":
                    for film in daftar_film:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            saldo = current_user["saldo"]
                            sisa_duid = current_user["saldo"] - isi["harga"] 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                            print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                            print("Terimas Kasih")
                            current_user["saldo"] = sisa_duid
                            simpan_data()
                            refresh_table_film()
                            return
                    else:
                        print("film tidak ditemukan!")
                elif metode.lower() == "e-pay":
                    for film in daftar_film:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            epay = current_user["e-pay"]
                            sisa_epay = current_user["e-pay"] - isi["harga"] 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                            print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                            print("Terima Kasih")
                            current_user["e-pay"] = sisa_epay
                            simpan_data()
                            refresh_table_film()
                            return
                    else:
                        print("film tidak ditemukan!")
                else:
                    print("metode pembayaran tidak ditemukan!")
        #untuk user vip di premier menggunakan saldo

    for user in data_user:
        if user['member'] == "VIP":
            isilah = input("Masukkan kode VIP: ")
            if user["kode member"] == isilah:
                if metode.lower() == "saldo":
                    for film in daftar_film:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            diskon_vip = int(harga_film - (harga_film * (30/ 100)))
                            saldo = current_user["saldo"]
                            sisa_duid = current_user["saldo"] - diskon_vip 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"Diskon : 30% Member VIP")
                            print(f"Total  : {format_uang(diskon_vip)}")
                            print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                            print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                            print("Terimas Kasih Sudah Berlangganan!")
                            current_user["saldo"] = sisa_duid
                            simpan_data()
                            refresh_table_film()
                            return
                        
                #untuk user vip di premier menggunakan e-pay
                elif metode.lower() == "e-pay":
                    for film in daftar_film:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            diskon_vip = int(harga_film - (harga_film * (30/ 100)))
                            epay = current_user["e-pay"]
                            sisa_epay = current_user["e-pay"] - diskon_vip 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"Diskon : 30% Member VIP")
                            print(f"Total  : {format_uang(diskon_vip)}")
                            print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                            print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                            print("Terimas Kasih Sudah Berlangganan!")
                            current_user["e-pay"] = sisa_epay
                            simpan_data()
                            refresh_table_film()
                            return
                    else:
                        print("film tidak ditemukan!")
                else:
                    print("metode pembayaran tidak ditemukan!")
            else:
                    print("Kode member salah!")

def premier():
    print(table2)
    print()
    print(" A1  A2  A3  A4      D6  D7  D8   D9")
    print(" B1  B2  B3  B4      E6  E7  E8   E9")
    print(" C1  C2  C3  C4      F6  F7  F8   F9")
    print("                                    ")
    print("----------------LAYAR---------------")
    print()

    while True:
        nomor = inputhandler("Pilih Film 01/02/03/04: ","digit")
        if len(nomor) < 2:
            print("Minimal 2 huruf")
        elif len(nomor) > 2:
            print("Maksimal 2 huruf")
        else:
            break
    while True:
        duduk = input("Pilih Seat: ")
        if len(duduk) < 2:
            print("Minimal 2 huruf")
        elif len(duduk) > 2:
            print("Maksimal 2 huruf")
        else:
            break
    metode = input("\nPilih metode pembayaran Saldo/E-pay: ")

    #untuk user biasa di premier menggunakan saldo
    for user in data_user:
        if user['member'] == "biasa": 
            isi = input("Apakah memiliki vaucher? y/n: ")
            if isi.lower() == "y":
                isi_lagi = input("Masukkan kode vaucher: ")
                for kode in voucher:
                    if kode["kode"] == isi_lagi:
                        if metode.lower() == "saldo":
                            for film in daftar_film_premier:
                                if film["nomor"] == nomor:
                                    isi = film
                                    nama_film = isi['film']
                                    harga_film = isi['harga']
                                    ket = kode["persen"]
                                    diskon = int(harga_film - (harga_film * (ket / 100)))
                                    saldo = current_user["saldo"]
                                    sisa_duid = current_user["saldo"] - diskon
                                    print("+---------------------------------+")
                                    print("|         INVOICE PREMIER!        |")
                                    print("+---------------------------------+")
                                    print(f"Film   : {nama_film}")
                                    print(f"Sheat  : {duduk}")
                                    print(f"Harga  : {format_uang(harga_film)}")
                                    print(f"Diskon : {ket}%")
                                    print(f"Total  : {format_uang(diskon)}")
                                    print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                                    print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                                    print("Terimas Kasih")
                                    kode['status'] = "Digunakan"
                                    current_user["saldo"] = sisa_duid
                                    simpan_data()
                                    refresh_table_film()
                                    return
                            else:
                                print("film tidak ditemukan!")
                        #untuk user biasa di premier menggunakan e-pay
                        elif metode.lower() == "e-pay":
                            for film in daftar_film_premier:
                                if film["nomor"] == nomor:
                                    isi = film
                                    nama_film = isi['film']
                                    harga_film = isi['harga']
                                    ket = kode["persen"]
                                    diskon = int(harga_film - (harga_film * (ket / 100)))
                                    epay = current_user["e-pay"]
                                    sisa_epay = current_user["e-pay"] - diskon
                                    print("+---------------------------------+")
                                    print("|         INVOICE PREMIER!        |")
                                    print("+---------------------------------+")
                                    print(f"Film   : {nama_film}")
                                    print(f"Sheat  : {duduk}")
                                    print(f"Harga  : {format_uang(harga_film)}")
                                    print(f"Diskon : {ket}%")
                                    print(f"Total  : {format_uang(diskon)}")
                                    print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                                    print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                                    print("Terimas Kasih")
                                    kode['status'] = "Digunakan"
                                    current_user["e-pay"] = sisa_epay
                                    simpan_data()
                                    refresh_table_film()
                                    return   
                            else:
                                print("film tidak ditemukan!")
                        else:
                            print("Metode pembayaran tidak ditemukan!")
                else:
                    print("Vaucher tidak dapat digunakan!")

            elif isi.lower() == "n":
                if metode.lower() == "saldo":
                    for film in daftar_film_premier:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            saldo = current_user["saldo"]
                            sisa_duid = current_user["saldo"] - isi["harga"] 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                            print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                            print("Terimas Kasih")
                            current_user["saldo"] = sisa_duid
                            simpan_data()
                            refresh_table_film()
                            return
                elif metode.lower() == "e-pay":
                    for film in daftar_film_premier:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            epay = current_user["e-pay"]
                            sisa_epay = current_user["e-pay"] - isi["harga"] 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                            print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                            print("Terima Kasih")
                            current_user["e-pay"] = sisa_epay
                            simpan_data()
                            refresh_table_film()
                            return
                    else:
                        print("film tidak ditemukan!")
                else:
                    print("metode pembayaran tidak ditemukan!")

        #untuk user vip di premier menggunakan saldo

    for user in data_user:
        if user['member'] == "VIP":
            isilah = input("Masukkan kode VIP: ")
            if user["kode member"] == isilah:
                if metode.lower() == "saldo":
                    for film in daftar_film_premier:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            diskon_vip = int(harga_film - (harga_film * (30/ 100)))
                            saldo = current_user["saldo"]
                            sisa_duid = current_user["saldo"] - diskon_vip 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"Diskon : 30% Member VIP")
                            print(f"Total  : {format_uang(diskon_vip)}")
                            print(f"\nSaldo Anda sekarang: {format_uang(saldo)}")
                            print(f"Sisa saldo Anda    : {format_uang(sisa_duid)}")
                            print("Terimas Kasih Sudah Berlangganan!")
                            current_user["saldo"] = sisa_duid
                            simpan_data()
                            refresh_table_film()
                            return
                
            #untuk user vip di premier menggunakan e-pay
                if metode.lower() == "e-pay":
                    for film in daftar_film_premier:
                        if film["nomor"] == nomor:
                            isi = film
                            nama_film = isi['film']
                            harga_film = isi['harga']
                            diskon_vip = int(harga_film - (harga_film * (30/ 100)))
                            epay = current_user["e-pay"]
                            sisa_epay = current_user["e-pay"] - diskon_vip 
                            print("+---------------------------------+")
                            print("|         INVOICE PREMIER!        |")
                            print("+---------------------------------+")
                            print(f"Film   : {nama_film}")
                            print(f"Sheat  : {duduk}")
                            print(f"Harga  : {format_uang(harga_film)}")
                            print(f"Diskon : 30% Member VIP")
                            print(f"Total  : {format_uang(diskon_vip)}")
                            print(f"\nE-pay Anda sekarang: {format_uang(epay)}")
                            print(f"Sisa e-pay Anda    : {format_uang(sisa_epay)}")
                            print("Terimas Kasih Sudah Berlangganan!")
                            current_user["e-pay"] = sisa_epay
                            simpan_data()
                            refresh_table_film()
                            return
                    else:
                        print("film tidak ditemukan!")
                else:
                    print("metode pembayaran tidak ditemukan!")
            else:
                print("Kode member salah!")

def tambah_saldo():
    while True:
        duit = inputhandler("Masukkan Saldo Anda: ", "int")
        if duit > 0:
            current_user["saldo"] += duit
            simpan_data()
            print(f"{format_uang(duit)} berhasil ditambah ke saldo anda\n")
            break
        else:
            print("\nTidak Bisa Negatif. Harap isi dengan benar!")

def epay(username):
    for user in data_user:
        if user["username"] == username:
            print(f"Saldo anda: {format_uang(user['saldo'])}")
            duitpay = inputhandler("Masukkan E-pay Anda: ", "int")
            if duitpay > 0:
                current_user["saldo"] -= duitpay
                current_user["e-pay"] += duitpay
                simpan_data()
                print(f"{format_uang(duitpay)} berhasil ditambah ke E-pay anda\n")
            else:
                print("\nTidak Bisa Negatif. Harap isi dengan benar!")


def info_akun(username):
    for user in data_user:
        if user["username"] == username:
            print(f"Username: {user['username']}")
            print(f"Member: {(user['member'])}")
            print(f"Saldo : {format_uang(user['saldo'])}")
            print(f"E-pay : {format_uang(user['e-pay'])}")
            if user['member'] == "biasa":
                print("\nAnda adalah member biasa. Apakah ingin upgrade ke member VIP?")
                print("Temukan keuntungan dengan member VIP!\n")
                print("[1] Buat akun VIP")
                print("[2] keluar")
                pilih = inputhandler("Pilih Menu: ", "int")
                if pilih == 1:
                    vip()
                elif pilih == 2:
                    menu()
            elif user['member'] == "VIP":
                print("\nAnda pengguna member VIP. Setiap transaksi anda dipotong 30%")
                print("Terima kasih!")

def vip():
    while True:
        for user in data_user:
            if user['member'] == "biasa":
                print("\nMembuat member dikenakan biaya awal sebesar Rp50.000")
                print("Pembayaran wajib menggunakan e-pay!\n")
                setuju = input("Apakah ande ingin menjadi member VIP? y/n: ")
                if setuju.lower() == "y":
                    kode_member = input("Buat kode: ")
                    current_user["e-pay"] -= 50000
                    user['member'] = "VIP"
                    user['kode member'] = kode_member
                    epay = user['e-pay']
                    simpan_data() #memanggil function tanpa perlu repot menulis program berulang ulang
                    print("\nSelamat Anda Sekarang adalah member VIP")
                    print(f"E-pay anda dipotong sebesar Rp50.000")
                    print(f"E-pay anda sekarang: {epay}")
                    menu()
                    break
                elif setuju.lower() == "n":
                    print("Member VIP dibatalkan!")
                    menu()
                else:
                    print("error")
#------------Menu-------------
def menu():

    while True:
        print("\n---------------------------------------")
        print("|             MENU UTAMA              |")
        print("---------------------------------------")
        print("|          [1] FILM REGULER           |")
        print("|          [2] FILM PREMIER           |")
        print("|          [3] ISI SALDO              |")
        print("|          [4] ISI E-PAY              |")
        print("|          [5] INFO AKUN              |")
        print("|          [6] KELUAR                 |")
        print("---------------------------------------")
        pilih = inputhandler("Pilih Menu: ", "int")
        if pilih == 1:
            print()
            reguler()
        elif pilih == 2:
            print()
            premier()
        elif pilih == 3:
            print()
            tambah_saldo()
        elif pilih == 4:
            print()
            epay(current_user["username"])
        elif pilih == 5:
            info_akun(current_user["username"])
        elif pilih == 6:
            print()
            print("Terima Kasih, anda telah keluar!")
            break
        else:
            print("Pilihan tidak ada!")


#------Tampilan awal----------
print("\n---------------------------------------")
print("|           SELAMAT DATANG DI         |")
print("---------------------------------------")
print("|         _BIOSKOP CINEMA XVI_        |")
print("--------------------------------------")
relog()
