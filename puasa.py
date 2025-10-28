from termcolor import colored, cprint

def ascii_art():
    print(colored("██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ███╗", 'yellow', attrs=['bold']))
    print(colored("██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗ ████║", 'yellow', attrs=['bold']))
    print(colored("███████║███████║██║     █████╔╝ ██║██╔████╔██║", 'yellow', attrs=['bold']))
    print(colored("██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╔╝██║", 'yellow', attrs=['bold']))
    print(colored("██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚═╝ ██║", 'yellow', attrs=['bold']))
    print(colored("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝", 'yellow', attrs=['bold']))
    print(colored("        MENU PEMBELAJARAN PUASA RAMADHAN     ", 'cyan', attrs=['bold']))
    print(colored("="*50, 'magenta'))

def tampilkan_nama_kelompok():
    print(colored("="*50, 'magenta'))
    print(colored("Kelompok 6 - Anggota:", 'green', attrs=['bold']))
    anggota = [
        "1. Rahmat Hidayat",
        "2. Raissa Putri",
        "3. Rakan Rizq",
        "4. Rara Tamiya",
        "5. Rajwa Nuha",
        "6. Rani Nurhamidah"
    ]
    for nama in anggota:
        print(colored(nama, 'yellow'))
    print(colored("="*50, 'magenta'))

def menu_utama():
    print(colored("\n[1] Membaca Teks & Kuis", 'cyan', attrs=['bold']))
    print(colored("[2] Sejarah Puasa Ramadhan", 'cyan', attrs=['bold']))
    print(colored("[3] Daftar Nama Kelompok", 'cyan', attrs=['bold']))
    print(colored("[0] Keluar", 'red', attrs=['bold']))

def membaca_teks_dan_kuis():
    paragraf = (
        "Puasa Ramadhan adalah ibadah wajib bagi umat Islam yang dilakukan selama bulan Ramadhan.\n"
        "Puasa berarti menahan diri dari makan, minum, dan hal-hal yang membatalkan puasa mulai dari\n"
        "terbit fajar hingga terbenam matahari. Selain menahan lapar dan dahaga, puasa juga melatih\n"
        "kesabaran, meningkatkan ketakwaan kepada Allah, serta mempererat rasa solidaritas sosial.\n"
        "Puasa Ramadhan juga menjadi waktu untuk memperbanyak ibadah, seperti shalat, membaca Al-Qur'an,\n"
        "dan berdoa. Dengan berpuasa, umat Islam diharapkan menjadi pribadi yang lebih baik dan bertakwa.\n"
    )
    print(colored("\n--- Materi Puasa Ramadhan ---", 'magenta', attrs=['bold']))
    print(colored(paragraf, 'white'))
    print(colored("--- Kuis Puasa Ramadhan ---", 'magenta', attrs=['bold']))

    pertanyaan = [
        {
            "tanya": "1. Apa arti puasa dalam konteks Ramadhan?",
            "jawab": "menahan diri"
        },
        {
            "tanya": "2. Kapan waktu pelaksanaan puasa dimulai dan berakhir setiap harinya?",
            "jawab": "terbit fajar hingga terbenam matahari"
        },
        {
            "tanya": "3. Sebutkan salah satu manfaat puasa selain menahan lapar dan dahaga!",
            "jawab": "melatih kesabaran"
        },
        {
            "tanya": "4. Ibadah apa yang dianjurkan untuk diperbanyak selama Ramadhan?",
            "jawab": "shalat"
        },
        {
            "tanya": "5. Apa tujuan utama dari berpuasa Ramadhan?",
            "jawab": "meningkatkan ketakwaan"
        }
    ]

    total_poin = 0
    for item in pertanyaan:
        jawaban_user = input(colored(item["tanya"] + "\nJawaban: ", 'yellow')).strip().lower()
        if item["jawab"] in jawaban_user:
            print(colored("Jawaban benar! +20 poin\n", 'green', attrs=['bold']))
            total_poin += 20
        else:
            print(colored("Jawaban salah. +0 poin\n", 'red', attrs=['bold']))

    print(colored(f"Total poin Anda: {total_poin} dari 100\n", 'cyan', attrs=['bold']))

def sejarah_puasa_ramadhan():
    teks_sejarah = (
        "Puasa Ramadhan memiliki sejarah yang sangat penting dalam Islam.\n"
        "Perintah berpuasa pertama kali diturunkan pada tahun kedua Hijriyah.\n"
        "Puasa ini diwajibkan sebagai salah satu rukun Islam yang harus dijalankan\n"
        "oleh setiap Muslim yang memenuhi syarat. Tujuan puasa adalah untuk mendidik\n"
        "jiwa agar menjadi lebih sabar dan bertakwa kepada Allah SWT. Selain itu,\n"
        "puasa juga menjadi sarana untuk meningkatkan solidaritas sosial dan empati\n"
        "terhadap orang-orang yang kurang beruntung. Dengan menjalankan puasa Ramadhan,\n"
        "umat Islam di seluruh dunia menunjukkan kepatuhan dan keimanan mereka kepada Allah.\n"
        "Puasa Ramadhan juga mempererat ukhuwah dan kebersamaan antar sesama muslim.\n"
    )
    print(colored("\n--- Sejarah Puasa Ramadhan ---", 'magenta', attrs=['bold']))
    print(colored(teks_sejarah, 'white'))

def tampilkan_nama_kelompok_lagi():
    print(colored("\n--- Daftar Nama Anggota Kelompok ---", 'magenta', attrs=['bold']))
    anggota = [
        "Rahmat Hidayat",
        "Raissa Putri",
        "Rakan Rizq",
        "Rara Tamiya",
        "Rajwa Nuha",
        "Rani Nurhamidah"
    ]
    for i, nama in enumerate(anggota, 1):
        print(colored(f"{i}. {nama}", 'yellow'))
    print()

def main():
    ascii_art()
    tampilkan_nama_kelompok()

    while True:
        menu_utama()
        pilihan = input(colored("Pilih menu (0-3): ", 'cyan', attrs=['bold'])).strip()

        if pilihan == "1":
            membaca_teks_dan_kuis()
        elif pilihan == "2":
            sejarah_puasa_ramadhan()
        elif pilihan == "3":
            tampilkan_nama_kelompok_lagi()
        elif pilihan == "0":
            print(colored("Terima kasih telah menggunakan program ini. Sampai jumpa!", 'green', attrs=['bold']))
            break
        else:
            print(colored("Pilihan tidak valid, silakan coba lagi.\n", 'red', attrs=['bold']))

if __name__ == "__main__":
    main()
