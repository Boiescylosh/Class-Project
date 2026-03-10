import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def header():
    print(Fore.YELLOW + Style.BRIGHT)
    print(r" $$$$$$\            $$\       $$\           $$\       ")
    print(r"$$  __$$\           \__|      $$ |          $$ |      ")
    print(r"$$ /  $$ | $$$$$$\  $$\  $$$$$$$ | $$$$$$\  $$$$$$$\  ")
    print(r"$$$$$$$$ |$$  __$$\ $$ |$$  __$$ | \____$$\ $$  __$$\ ")
    print(r"$$  __$$ |$$ /  $$ |$$ |$$ /  $$ | $$$$$$$ |$$ |  $$ |")
    print(r"$$ |  $$ |$$ |  $$ |$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |")
    print(r"$$ |  $$ |\$$$$$$$ |$$ |\$$$$$$$ |\$$$$$$$ |$$ |  $$ |")
    print(r"\__|  \__| \____$$ |\__| \_______| \_______|\__|  \__|")
    print(r"                $$ |                                  ")
    print(r"                $$ |                                  ")
    print(r"                \__|                                  ")
    print(Style.RESET_ALL)
    print(Fore.CYAN + "[T] [o] [o] [l]   [K] [e] [l] [o] [m] [p] [o] [k]")
    print()

def warning():
    print(Fore.RED + Style.BRIGHT + "[!] Tugas Kelompok [!]")
    print(Style.RESET_ALL)

def menu():
    print(Fore.GREEN + Style.BRIGHT + "\nMenu:")
    print(Fore.YELLOW + "[1] Materi Aqidah")
    print(Fore.YELLOW + "[2] Sejarah Aqidah")
    print(Fore.YELLOW + "[3] Tampilkan Nama Kelompok")
    print(Fore.RED + "[0] Keluar")
    print(Style.RESET_ALL)

# Silakan ganti nama anggota di sini
anggota = ["Nama1", "Nama2", "Nama3"]

def tampilkan_nama_kelompok():
    print(Fore.CYAN + Style.BRIGHT + "\n=== Daftar Anggota Kelompok ===")
    for nama in anggota:
        print(Fore.WHITE + " - " + nama)
    print(Fore.CYAN + "===============================")

def materi_aqidah():
    print(Fore.MAGENTA + "\n[Materi Aqidah]")
    print(Fore.WHITE + "Aqidah secara bahasa berarti ikatan atau keyakinan yang kokoh.")
    print(Fore.WHITE + "Isi materi lengkap bisa kamu tambahkan di sini...")

def sejarah_aqidah():
    print(Fore.MAGENTA + "\n[Sejarah Aqidah]")
    print(Fore.WHITE + "Sejarah perkembangan aqidah dari masa Rasulullah hingga saat ini.")
    print(Fore.WHITE + "Isi sejarah lengkap bisa kamu tambahkan di sini...")

def main():
    header()
    warning()
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
            print(Fore.GREEN + "\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
