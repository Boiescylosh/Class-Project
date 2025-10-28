import os
import time
from colorama import init, Fore, Style

# Inisialisasi colorama untuk warna
init(autoreset=True)

def clear():
    os.system('clear')

def tampil_piramida():
    print(Fore.YELLOW + Style.BRIGHT + r"""
           ▒
          ▒▒▒
         ▒▒▒▒▒
        ▒▒▒▒▒▒▒
       ▒▒▒▒▒▒▒▒▒
      ▒▒▒▒▒▒▒▒▒▒▒
     ▒▒▒▒▒▒▒▒▒▒▒▒▒
    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
       HAJI&UMROH
    """ + Style.RESET_ALL)

def tampil_kelompok():
    print(Fore.CYAN + "=== KELOMPOK PEMBELAJARAN ===")
    anggota = [
        "Paiz Efendi Nurjen",
        "Rina Yulianingtiyas Hajir",
        "Risda Salsabila Zaini",
        "Riza Nurrohim",
        "Rizal Abdul Malik",
        "Rizal Mubarok"
    ]
    for i, nama in enumerate(anggota, 1):
        print(f"{i}. {nama}")
    print("=" * 35)

def menu_1():
    clear()
    print(Fore.BLUE + "=== MATERI HAJI DAN UMROH ===")
    print("""
Haji dan Umroh adalah ibadah penting dalam Islam.
Haji dilaksanakan pada bulan Dzulhijjah setiap tahun.
Umroh bisa dilaksanakan kapan saja sepanjang tahun.
Keduanya dilakukan di kota suci Mekkah, Arab Saudi.
Thawaf, sa’i, dan tahallul adalah bagian dari ritualnya.
Haji hukumnya wajib bagi yang mampu, Umroh sunnah.
Ibadah ini menumbuhkan ketakwaan dan persatuan umat.
""")
    print(Fore.YELLOW + "\n=== Jawablah pertanyaan berikut (benar = 20 poin):\n")

    soal = [
        ("1. Haji dilaksanakan pada bulan apa?", "Dzulhijjah"),
        ("2. Umroh dapat dilakukan kapan?", "Kapan saja"),
        ("3. Apa saja ritual yang dilakukan dalam Haji dan Umroh?", "Thawaf"),
        ("4. Apa hukum Haji bagi yang mampu?", "Wajib"),
        ("5. Apa hikmah dari Haji dan Umroh?", "Persatuan")
    ]

    poin = 0
    for tanya, jawaban in soal:
        jawaban_user = input(tanya + " ").strip().lower()
        if jawaban.lower() in jawaban_user:
            print(Fore.GREEN + "✓ Benar!\n")
            poin += 20
        else:
            print(Fore.RED + f"✗ Salah. Jawaban yang benar: {jawaban}\n")

    print(Fore.CYAN + f"Total Skor: {poin} dari 100\n")
    input("Tekan ENTER untuk kembali ke menu...")

def menu_2():
    clear()
    print(Fore.MAGENTA + "=== SEJARAH HAJI DAN UMROH ===\n")
    print("""
Ibadah Haji pertama kali diperintahkan kepada Nabi Ibrahim.
Beliau membangun Ka'bah bersama anaknya Nabi Ismail.
Ka'bah menjadi pusat ibadah dan ziarah umat Islam hingga kini.
Setelah itu, tradisi ini dilanjutkan oleh umat setelahnya.
Pada masa Nabi Muhammad, ibadah Haji disempurnakan syariatnya.
Rasulullah menunaikan Haji Wada' sebagai haji terakhirnya.
Sejak saat itu, jutaan Muslim berhaji setiap tahunnya.
Umroh juga dilakukan oleh Nabi Muhammad pada masa damai.
Haji dan Umroh menjadi bagian penting rukun Islam kelima.
Mereka yang berhaji disebut sebagai tamu Allah SWT.
""")
    input("\nTekan ENTER untuk kembali ke menu...")

def menu_3():
    clear()
    tampil_kelompok()
    input("\nTekan ENTER untuk kembali ke menu...")

def main():
    while True:
        clear()
        tampil_piramida()
        tampil_kelompok()
        print(Fore.YELLOW + "\n=== MENU PEMBELAJARAN ===")
        print("1. Membaca Teks dan Kuis")
        print("2. Sejarah Haji dan Umroh")
        print("3. Lihat Nama Kelompok")
        print("0. Keluar\n")

        pilihan = input("Pilih menu (0-3): ")
        if pilihan == '1':
            menu_1()
        elif pilihan == '2':
            menu_2()
        elif pilihan == '3':
            menu_3()
        elif pilihan == '0':
            print(Fore.RED + "Terima kasih. Program selesai.")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid!")
            time.sleep(1)

# Jalankan program
main()
