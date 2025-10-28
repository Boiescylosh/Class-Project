from termcolor import colored, cprint

def tampilkan_nama_kelompok():
    cprint("Kelompok 6 Anggota:", "yellow", attrs=["bold"])
    anggota = [
        "1. Nur Hikmah Aprilia",
        "2. Nur Fitri Fauziyah",
        "3. Nuraeni Munawwaroh",
        "4. Nur Ica Fiqurasyin",
        "5. Nita Suhaeniah",
        "6. Nur Aini"
    ]
    for nama in anggota:
        cprint(nama, "cyan")
    print("\n")

def tampilkan_menu():
    cprint("Menu:", "green", attrs=["bold"])
    cprint("1. Membaca Teks Materi Konstatinovel dan Quiz", "magenta")
    cprint("2. Membaca Teks Sejarah Konstatinovel", "magenta")
    cprint("3. Tampilkan Nama Anggota Kelompok", "magenta")
    cprint("0. Keluar", "red", attrs=["bold"])

def materi_konstatinovel():
    cprint("\nMateri Konstatinovel:", "yellow", attrs=["bold"])
    paragraf = [
        "Konstatinovel adalah sebuah konsep dalam dunia sastra...",
        "Konsep ini menekankan pada stabilitas tema dan karakter...",
        "Dalam konstatinovel, penulis berusaha menjaga konsistensi...",
        "Unsur konstanta ini membuat cerita menjadi mudah diikuti...",
        "Biasanya, konstatinovel digunakan untuk genre fiksi tertentu...",
        "Keunikan konstatinovel adalah pada perpaduan antara stabilitas dan kreativitas."
    ]
    for p in paragraf:
        cprint(p, "white")

def main():
    cprint("HACKING TOOL", "yellow", attrs=["bold"])
    cprint("[!] This Tool is Only For Educational Purpose Please Don't use for Any illegal Activity [!]", "red", attrs=["bold"])
    cprint("[!] This Tool Must Run as a Root...[!]", "red")
    while True:
        tampilkan_menu()
        pilihan = input(colored("Pilih menu: ", "cyan"))
        if pilihan == "1":
            materi_konstatinovel()
        elif pilihan == "2":
            cprint("Teks Sejarah Konstatinovel...", "white")
        elif pilihan == "3":
            tampilkan_nama_kelompok()
        elif pilihan == "0":
            cprint("Keluar...", "red")
            break
        else:
            cprint("Pilihan tidak valid!", "red")

if __name__ == "__main__":
    main()
