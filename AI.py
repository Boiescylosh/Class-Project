import os
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

COLOR_LIST = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE
]

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def random_color():
    return random.choice(COLOR_LIST) + Style.BRIGHT

def print_banner():
    color = random_color()
    print(color + "                █████╗    ██║                  ")
    print(color + "               ██╔══██╗   ██║                    ")
    print(color + "               ███████║   ██║                     ")
    print(color + "               ██╔══██║   ██║                    ")
    print(color + "               ██║  ██║   ██║                    ")
    print(color + "                                                      ")
    print(color + "           WELCOME TO AI KELAS 6D")
    print()
    print(Fore.CYAN + Style.BRIGHT + "[ Belajar Sejarah Kecerdasan Buatan Yuk! ]")
    print(Fore.RED + Style.BRIGHT + "──────────────────────────────────────────")
    print()

def print_menu():
    print(Fore.CYAN + Style.BRIGHT + "[::] Pilih Menu Pembelajaran [::]")
    print(Fore.YELLOW + "[01] Pengantar dan Penjelasan AI")
    print(Fore.YELLOW + "[02] Sejarah Singkat AI + Pertanyaan")
    print(Fore.YELLOW + "[03] Pembelajaran Lanjutan tentang AI")
    print(Fore.YELLOW + "[04] Anggota Kelompok")
    print(Fore.RED + "[00] Keluar")
    print()

def pengantar_ai(nama):
    clear()
    print(Fore.GREEN + f"Halo {nama}, Selamat datang di dunia Artificial Intelligence!")
    time.sleep(1)
    print()
    print(Fore.CYAN + Style.BRIGHT + "Artificial Intelligence (AI) adalah bidang dalam ilmu komputer yang berfokus pada penciptaan sistem yang dapat melakukan tugas-tugas yang biasanya membutuhkan kecerdasan manusia.")
    print(Fore.CYAN + "Contohnya seperti pengenalan wajah, suara, pengambilan keputusan, dan lain-lain.")
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk kembali ke menu...")

def sejarah_ai():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "[ SEJARAH SINGKAT ARTIFICIAL INTELLIGENCE ]")
    print()
    print(Fore.CYAN + "Kecerdasan Buatan mulai diperkenalkan pada tahun 1956 dalam sebuah konferensi di Dartmouth College.")
    print(Fore.CYAN + "Tokoh penting seperti John McCarthy, Marvin Minsky, dan Allen Newell merupakan pelopor AI.")
    print(Fore.CYAN + "Pada awalnya, AI difokuskan pada pemecahan masalah logika dan matematika sederhana.")
    print(Fore.CYAN + "Seiring berkembangnya teknologi, AI mulai digunakan dalam banyak bidang seperti kesehatan, industri, dan pendidikan.")
    print(Fore.CYAN + "Kini, AI telah menjadi bagian penting dalam kehidupan sehari-hari melalui smartphone, mobil, dan internet.")
    print()

    print(Fore.YELLOW + Style.BRIGHT + "Jawablah pertanyaan berikut ini berdasarkan paragraf di atas:\n")
    pertanyaan = [
        "1. Kapan AI pertama kali diperkenalkan?",
        "2. Siapa salah satu tokoh penting dalam perkembangan AI?",
        "3. Pada awalnya, AI digunakan untuk menyelesaikan masalah apa?",
        "4. Sebutkan salah satu bidang yang sekarang menggunakan AI!",
        "5. Contoh teknologi yang menggunakan AI dalam kehidupan sehari-hari?"
    ]
    for tanya in pertanyaan:
        input(Fore.CYAN + tanya + "\n> ")

    print(Fore.GREEN + "\nTerima kasih telah menjawab! Yuk lanjut belajar AI!")
    input(Fore.YELLOW + "\nTekan ENTER untuk kembali ke menu...")

def pembelajaran_lanjutan():
    clear()
    print(Fore.GREEN + Style.BRIGHT + "[ PEMBELAJARAN LANJUTAN: CABANG-CABANG AI ]")
    print()
    print(Fore.CYAN + "- Machine Learning: Mengajarkan mesin belajar dari data.")
    print(Fore.CYAN + "- Natural Language Processing: Memahami dan memproses bahasa manusia.")
    print(Fore.CYAN + "- Computer Vision: Mengenali gambar dan visual.")
    print(Fore.CYAN + "- Robotics: Menciptakan robot cerdas.")
    print(Fore.CYAN + "- Expert Systems: Sistem berbasis pengetahuan untuk pengambilan keputusan.")
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk kembali ke menu...")

def tampilkan_anggota():
    print(Fore.CYAN + Style.BRIGHT + "[::] KELOMPOK 3 AI [::]")
    anggota_list = [
        "1. Razaqhi Nur Hafizh",
        "2. Regi Aditya",
        "3. Rere Sutari",
        "4. Reyna Nabila",
        "5. Rezal Nurul Bahtiar",
        "6. Ridwan Hafidz"
    ]
    for anggota in anggota_list:
        print(Fore.YELLOW + anggota)
    print()
    input(Fore.YELLOW + "Tekan ENTER untuk kembali ke menu...")

def main():
    while True:
        clear()
        print_banner()
        nama = input(Fore.CYAN + "Masukan Nama Anda: ")
        print()
        print_menu()
        try:
            pilihan = int(input(Fore.CYAN + "Pilih opsi: "))
        except ValueError:
            print(Fore.RED + "Input tidak valid!")
            time.sleep(1)
            continue

        if pilihan == 1:
            pengantar_ai(nama)
        elif pilihan == 2:
            sejarah_ai()
        elif pilihan == 3:
            pembelajaran_lanjutan()
        elif pilihan == 4:
            clear()
            tampilkan_anggota()
        elif pilihan == 0:
            print(Fore.GREEN + "Keluar. Terima kasih dan sampai jumpa!")
            break
        else:
            print(Fore.RED + "Pilihan tidak tersedia!")
            time.sleep(1)
        input(Fore.YELLOW + "\nTekan ENTER untuk kembali ke menu...")

if __name__ == "__main__":
    main()

