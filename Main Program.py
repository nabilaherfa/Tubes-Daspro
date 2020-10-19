print()
print("----------   TUGAS BESAR   ----------")
print("      DASAR PEMROGRAMAN (IF1210)     ")
print("              Kelas 08               ")
print("            Kelompok 06              ")
print("  1. Nabilah Erfariani (16519108)    ")
print("  2. M. Hanif A. Nasution (16519298) ")
print("  3. M. Reza Nur Fauzi (16519308)    ")
print("  4. Bintang Fajarianto (16519498)   ")
print()

# Load 7 Database
from F01_Load_File import (array_user, array_wahana, array_pembelian_tiket, array_penggunaan_tiket, array_kepemilikan_tiket, array_refund_tiket, array_kritik_saran)

# Import File Utama
import F02_Login_User
import F03_Save_File
import F04_Sign_Up_User
import F05_Pencarian_Pemain
import F06_Pencarian_Wahana
import F07_Pembelian_Tiket
import F08_Menggunakan_Tiket
import F09_Refund
import F10_Kritik_dan_Saran
import F11_Melihat_Kritik_dan_Saran
import F12_Menambahkan_Wahana
import F13_Top_Up_Saldo
import F14_Melihat_Riwayat_Penggunaan_Wahana
import F15_Melihat_Jumlah_Tiket_Pemain
import F16_Exit
import B02_Golden_Account
import B03_Best_Wahana
import B04_Laporan_Kehilangan_Tiket

# Fungsi untuk menjawab pertanyaan optional iya atau tidak
def Opsi(bool):
    print('(1) iya')
    print('(2) tidak')

    pilihan = 99
    while pilihan == 99:
        inputan = input('Masukkan menu pilihanmu (1/2): ')
        try:
            inputan = int(inputan)
        except ValueError:
            print("\nMasukan tidak valid. Harap masukkan pilihan yang benar!\n")
            continue
        if not (1 <= inputan <= 2):
            print("\nMasukan tidak valid. Harap masukkan pilihan yang benar!\n")
            continue
        pilihan = inputan

    lanjut = bool
    if pilihan == 1:
        lanjut = True
    else:
        lanjut = False
    return lanjut

# Fungsi untuk menentukan aktivitas apa saja yang dapat dilakukan Admin
def aktivitasAdmin(nama):
    print('\nBerikut adalah menu-menu yang dapat kamu gunakan:')
    print('(1) Sign Up Pemain Baru.')
    print('(2) Pencarian pemain.')
    print('(3) Pencarian Wahana.')
    print('(4) Best Wahana.')
    print('(5) Daftar Kritik dan Saran.')
    print('(6) Tambah Wahana.')
    print('(7) Top-Up Saldo Pemain.')
    print('(8) Upgrade Pemain.')
    print('(9) Riwayat Penggunaan Wahana.')
    print('(10) Daftar Jumlah Tiket Pemain.')
    print('(11) Exit.')
    print('')

    menu = 99
    while menu == 99:
        inputan = input('Masukkan menu pilihanmu (1/2/3/4/5/6/7/8/9/10/11): ')
        try:
            inputan = int(inputan)
        except ValueError:
            print("\nMasukan tidak valid. Silakan pilih menu yang benar!\n")
            continue
        if not (1 <= inputan <= 11):
            print("\nMasukan tidak valid. Silakan pilih menu yang benar!\n")
            continue
        menu = inputan

    return menu

# Fungsi untuk menentukan apa saja yang dapat dilakukan Pemain
def aktivitasPemain(nama):
    print('\nBerikut menu-menu yang dapat kamu gunakan:')
    print('(1) Cari Wahana.')
    print('(2) Best Wahana.')
    print('(3) Beli Tiket.')
    print('(4) Gunakan Tiket.')
    print('(5) Refund Tiket.')
    print('(6) Laporan Kehilangan Tiket.')
    print('(7) Kritik dan Saran.')
    print('(8) Exit.')

    menu = 99
    while menu == 99:
        inputan = input('Masukkan menu pilihanmu (1/2/3/4/5/6/7/8): ')
        try:
            inputan = int(inputan)
        except ValueError:
            print("\nMasukan tidak valid. Silakan pilih menu yang benar!\n")
            continue
        if not (1 <= inputan <= 8):
            print("\nMasukan tidak valid. Silakan pilih menu yang benar!\n")
            continue
        menu = inputan
    return menu

# PROGRAM UTAMA
lanjutProgram = True
while lanjutProgram:
    # Opening
    print()
    print('🎈 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 🎈')
    print('🎈                    SELAMAT DATANG                    🎈')
    print('🎈            di Wahana Bermain Willy Wangky!           🎈')
    print('🎈 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 🎈')
    print()

    # Log in User
    print('Silakan masukkan username dan passwordmu!')
    print('Jika kamu belum memiliki akun, silakan hubungi admin kami untuk proses pendaftaran.')
    print()
    valid_login = False
    while not(valid_login):
        valid_login, Username = F02_Login_User.loginUser(array_user)

    # Mencari Nama dan Role User
    barisUser = 0
    while(array_user[barisUser][0] != ''):
        barisUser += 1

    foundRole = False
    idx_user = 0
    while (idx_user < barisUser) and not(foundRole):
        if Username == array_user[idx_user][3]:
            Role = array_user[idx_user][5]
            Nama = array_user[idx_user][0]
            foundRole = True
        else:
            idx_user += 1

    # Menentukan aktivitas User
    signOut = False
    while (Role == 'Admin') and not(signOut):
        pilih_menu = aktivitasAdmin(Nama)
        if pilih_menu == 1:
            Ulang = True
            while Ulang:
                dataUserBaru = array_user
                dataUserBaru = F04_Sign_Up_User.signUpUser(dataUserBaru)
                print('\nApakah kamu mau menambahkan pemain lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau menyimpan sementara data tersebut?')
            jawaban = Opsi(Ulang)
            if jawaban == True:
                array_user = dataUserBaru
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 2:
            Ulang = True
            while Ulang:
                F05_Pencarian_Pemain.cariPemain(array_user)
                print('\nApakah kamu mau mencari pemain lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 3:
            Ulang = True
            while Ulang:
                F06_Pencarian_Wahana.cariWahana(array_wahana)
                print('\nApakah kamu mau mencari wahana lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 4:
            B03_Best_Wahana.bestWahana(array_wahana, array_penggunaan_tiket)
            Ulang = True
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 5:
            F11_Melihat_Kritik_dan_Saran.melihatKdanS(Username, array_user, array_kritik_saran)
            Ulang = True
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 6:
            Ulang = True
            while Ulang:
                dataWahanaBaru = array_wahana
                dataWahanaBaru = F12_Menambahkan_Wahana.tambahWahana(dataWahanaBaru)
                print('\nApakah kamu mau menambahkan wahana lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau menyimpan sementara data tersebut?')
            jawaban = Opsi(Ulang)
            if jawaban == True:
                array_wahana = dataWahanaBaru
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 7:
            array_user = F13_Top_Up_Saldo.topUpSaldo(array_user)
            Ulang = True
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 8:
            Ulang = True
            while Ulang:
                array_user = B02_Golden_Account.goldenAccount(array_user)
                print('\nApakah kamu mau meng-upgrade pemain lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 9:
            F14_Melihat_Riwayat_Penggunaan_Wahana.riwayatPenggunaanWahana(array_penggunaan_tiket)
            Ulang = True
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 10:
            F15_Melihat_Jumlah_Tiket_Pemain.lihatJmlTiket(array_kepemilikan_tiket, array_wahana)
            Ulang = True
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 11:
            F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
            signOut = True

    while ((Role == 'Pemain') or (Role == 'Golden Pemain')) and not(signOut):
        pilih_menu = aktivitasPemain(Nama)
        if pilih_menu == 1:
            Ulang = True
            while Ulang:
                F06_Pencarian_Wahana.cariWahana(array_wahana)
                print('\nApakah kamu mau mencari wahana lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 2:
            B03_Best_Wahana.bestWahana(array_wahana, array_penggunaan_tiket)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            Ulang = True
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 3:
            Ulang = True
            while Ulang:
                array_user, array_kepemilikan_tiket, array_pembelian_tiket = F07_Pembelian_Tiket.pembelianTiket(Username,array_wahana,array_user,array_kepemilikan_tiket,array_pembelian_tiket)
                print('\nApakah kamu mau beli tiket wahana lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 4:
            Ulang = True
            while Ulang:
                array_penggunaan_tiket, array_kepemilikan_tiket = F08_Menggunakan_Tiket.gunakanTiket(array_penggunaan_tiket,array_kepemilikan_tiket,Username)
                print('\nApakah kamu bermain wahana lain?')
                Ulang = Opsi(Ulang)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 5:
            array_user, array_kepemilikan_tiket, array_refund_tiket = F09_Refund.refundTiket(array_user,array_wahana,array_kepemilikan_tiket,array_refund_tiket,Username)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            Ulang = True
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 6:
            array_kepemilikan_tiket = B04_Laporan_Kehilangan_Tiket.laporanKehilanganTiket(array_kepemilikan_tiket)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            Ulang = True
            jawaban = Opsi(Ulang)
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 7:
            array_kritik_saran = F10_Kritik_dan_Saran.kritikSaran(array_kritik_saran, Username)
            print('\nApakah kamu mau melakukan aktivitas yang lain?')
            jawaban = Opsi(Ulang)
            Ulang = True
            if jawaban == False:
                F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
                signOut = True

        elif pilih_menu == 8:
            F16_Exit.exit(array_user,array_wahana,array_pembelian_tiket,array_penggunaan_tiket, array_kepemilikan_tiket,array_refund_tiket,array_kritik_saran)
            signOut = True

    print('\nLanjutkan Program?')
    lanjutProgram = Opsi(lanjutProgram)

if lanjutProgram == False: # Gak Akan Stop Program Ini
    print('\nTerima kasih sudah menjalankan program kami 😄!\n')