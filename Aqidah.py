import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def header():
    print(Fore.YELLOW + Style.BRIGHT)
    print(" _   _      _ _         _   _             ")
    print("| | | | ___| | | ___   | | | | ___  _ __  ")
    print("| |_| |/ _ \ | |/ _ \  | |_| |/ _ \| '_ \ ")
    print("|  _  |  __/ | | (_) | |  _  | (_) | | | |")
    print("|_| |_|\___|_|_|\___/  |_| |_|\___/|_| |_|")
    print(Style.RESET_ALL)
    print(Fore.CYAN + "[T] [o] [o] [l]   [K] [e] [l] [o] [m] [p] [o] [k]")
    print()

def warning():
    print(Fore.RED + Style.BRIGHT + "[!] Tool ini hanya untuk pembelajaran. Jangan gunakan untuk aktivitas ilegal! [!]")
    print(Style.RESET_ALL)

def menu():
    print(Fore.GREEN + Style.BRIGHT + "\nMenu:")
    print(Fore.YELLOW + "[1] Materi Aqidah")
    print(Fore.YELLOW + "[2] Sejarah Aqidah")
    print(Fore.YELLOW + "[3] Tampilkan Nama Kelompok")
    print(Fore.RED + "[0] Keluar")
    print(Style.RESET_ALL)

anggota = ["Nama1", "Nama2", "Nama3"]

def tampilkan_nama_kelompok():
    print(Fore.CYAN + Style.BRIGHT + "\nDaftar Anggota Kelompok:")
    for nama in anggota:
        print(Fore.WHITE + "- " + nama)
    print(Style.RESET_ALL)

def materi_aqidah():
    print(Fore.MAGENTA + "Materi Aqidah: ... (isi materi di sini)")

def sejarah_aqidah():
    print(Fore.MAGENTA + "Sejarah Aqidah: ... (isi sejarah di sini)")

def main():
    header()
    warning()
    tampilkan_nama_kelompok()
    while True:
        menu()
        pilihan = input(Fore.BLUE + "Pilih menu (0-3): " + Style.RESET_ALL)
        if pilihan == "1":
            materi_aqidah()
        elif pilihan == "2":
            sejarah_aqidah()
        elif pilihan == "3":
            tampilkan_nama_kelompok()
        elif pilihan == "0":
            print(Fore.GREEN + "Terima kasih telah menggunakan program ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
