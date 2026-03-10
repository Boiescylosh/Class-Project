from termcolor import colored, cprint

def tampilkan_header():

    ascii_art = r"""
  __    __     __       ________   ___________      ______      _______    ___  ___  
 /" |  | "\   |" \     /"       ) ("     _   ")    /    " \    /"      \  |"  \/"  | 
(:  (__)  :)  ||  |   (:   \___/   )__/  \\__/    // ____  \  |:        |  \   \  /  
 \/      \/   |:  |    \___  \        \\_ /      /  /    ) :) |_____/   )   \\  \/   
 //  __  \\   |.  |     __/  \\       |.  |     (: (____/ //   //      /    /   /    
(:  (  )  :)  /\  |\   /" \   :)      \:  |      \        /   |:  __   \   /   /     
 \__|  |__/  (__\_|_) (_______/        \__|       \"_____/    |__|  \___) |___/      
    """
    cprint(ascii_art, "yellow", attrs=["bold"])
    cprint("="*85, "yellow")
    cprint("KELOMPOK 5 BJIR".center(85), "yellow", attrs=["bold"])
    cprint("[!] Tugas Kuliah ih sebel [!]".center(85), "red", attrs=["bold"])
    cprint("[!] Beauty Girls...[!]".center(85), "light_magenta")
    cprint("="*85, "yellow")

def tampilkan_nama_kelompok():
    print("\n")
    cprint("--- Anggota Kelompok 6 ---", "cyan", attrs=["bold"])
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
    cprint("\n>>> Menu Utama:", "green", attrs=["bold"])
    cprint("[1] Membaca Teks Materi Konstantinopel dan Quiz", "magenta")
    cprint("[2] Membaca Teks Sejarah Konstantinopel", "magenta")
    cprint("[3] Tampilkan Nama Anggota Kelompok", "magenta")
    cprint("[0] Keluar", "red", attrs=["bold"])

def materi_Konstatinopel():
    cprint("\nMateri Konstantinopel:", "yellow", attrs=["bold"])
    paragraf = [
        "Konstantinopel adalah ibu kota Kekaisaran Romawi Timur...",
        "Kota ini dikenal karena pertahanannya yang sangat kuat (Tembok Theodosius)...",
        "Penaklukan kota ini oleh Muhammad Al-Fatih pada 1453 mengubah sejarah dunia.",
        "Setelah jatuh ke tangan Ottoman, namanya berubah menjadi Istanbul.",
        "Keunikan Konstantinopel adalah letaknya yang strategis di antara Asia dan Eropa."
    ]
    for p in paragraf:
        cprint(f"   {p}", "white")

def main():
    tampilkan_header()
    while True:
        tampilkan_menu()
        pilihan = input(colored("\nPilih nomor menu: ", "cyan"))
        
        if pilihan == "1":
            materi_Konstatinopel()
        elif pilihan == "2":
            cprint("\nTeks Sejarah Konstantinopel:", "yellow", attrs=["bold"])
            cprint("   Konstantinopel didirikan oleh Kaisar Konstantinus Agung...", "white")
        elif pilihan == "3":
            tampilkan_nama_kelompok()
        elif pilihan == "0":
            cprint("\nSampai jumpa...", "red", attrs=["bold"])
            break
        else:
            cprint("Pilihan tidak valid, coba lagi", "red")

if __name__ == "__main__":
    main()
