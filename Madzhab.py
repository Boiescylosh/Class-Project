from colorama import Fore, Style, init
from pyfiglet import Figlet

init(autoreset=True)

def garis():
    print(Fore.YELLOW + "="*60)

def tampil_ascii():
    f = Figlet(font='big')
    print(Fore.LIGHTYELLOW_EX + f.renderText('MADZHAB TOOL'))

def tampil_kelompok(kelompok):
    print(Fore.CYAN + "Nama Kelompok:")
    for anggota in kelompok:
        print(Fore.GREEN + f"- {anggota}")

def tampil_menu():
    print(Fore.MAGENTA + "\n[1] Membaca Teks")
    print(Fore.MAGENTA + "[2] Sejarah Madzhab")
    print(Fore.MAGENTA + "[3] Nama-nama Kelompok")
    print(Fore.MAGENTA + "[0] Keluar")

def main():
    kelompok = ["Nasywa Mufidah", "Naura Firda", "Neneng Novita", "Neng Feby"]
    tampil_ascii()
    garis()
    tampil_kelompok(kelompok)
    garis()
    while True:
        tampil_menu()
        pilihan = input(Fore.YELLOW + "\nPilih nomor menu (1-3, 0 untuk keluar): ")

        if pilihan == '1':
            materi_madzhab = Fore.WHITE + '''
Madzhab adalah suatu aliran atau mazhab dalam Islam yang berisi
pendapat para ulama dalam memahami dan mengamalkan ajaran Islam.
Terdapat beberapa madzhab yang diikuti oleh umat Islam di seluruh dunia,
seperti Madzhab Hanafi, Maliki, Syafi'i, dan Hanbali.
Setiap madzhab memiliki metode dan pendekatan yang berbeda dalam
menafsirkan Al-Qur'an dan Hadis.
Madzhab berperan penting dalam menjaga keberagaman dan kesatuan umat Islam.
'''
            pertanyaan = [
                "Apa itu Madzhab?",
                "Sebutkan salah satu madzhab yang diikuti umat Islam!",
                "Apa peran madzhab dalam Islam?",
                "Berapa jumlah madzhab utama dalam Islam?",
                "Apa yang membedakan setiap madzhab?"
            ]
            jawaban_benar = [
                "suatu aliran atau mazhab dalam islam",
                "hanafi",
                "menjaga keberagaman dan kesatuan umat islam",
                "4",
                "metode dan pendekatan yang berbeda"
            ]
            poin = 0
            garis()
            print(Fore.LIGHTWHITE_EX + "Materi Madzhab:")
            print(materi_madzhab)
            garis()
            for i, tanya in enumerate(pertanyaan, 1):
                jawaban = input(Fore.CYAN + f"{i}. {tanya} ")
                if jawaban.lower().strip() == jawaban_benar[i-1]:
                    poin += 20
                    print(Fore.GREEN + "Jawaban benar! +20 poin")
                else:
                    print(Fore.RED + "Jawaban salah! +0 poin")
            garis()
            print(Fore.YELLOW + f"Total poin: {poin}")
            garis()

        elif pilihan == '2':
            sejarah_madzhab = Fore.WHITE + '''
Madzhab dalam Islam bermula dari masa Nabi Muhammad SAW dan para sahabatnya.
Setelah wafatnya Nabi, para ulama mulai mengembangkan pemahaman ajaran Islam.
Madzhab muncul sebagai hasil ijtihad para ulama dalam menafsirkan Al-Qur'an dan Hadis.
Empat madzhab utama yang dikenal adalah Hanafi, Maliki, Syafi'i, dan Hanbali.
Setiap madzhab memiliki ciri khas dan metode tersendiri dalam memahami syariat.
Madzhab berperan penting dalam menjaga kesatuan umat Islam meskipun berbeda pendapat.
Sejarah madzhab mencerminkan dinamika intelektual dan keagamaan umat Islam.
Madzhab juga menjadi sumber hukum Islam yang diikuti oleh mayoritas umat.
Perkembangan madzhab terus berlangsung hingga saat ini dengan berbagai cabang.
Pemahaman madzhab membantu umat Islam dalam menjalankan ajaran agama secara benar.
'''
            garis()
            print(Fore.LIGHTWHITE_EX + "Sejarah Madzhab:")
            print(sejarah_madzhab)
            garis()

        elif pilihan == '3':
            garis()
            tampil_kelompok(kelompok)
            garis()
        elif pilihan == '0':
            print(Fore.LIGHTRED_EX + "Terima kasih! Keluar dari program...")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, silakan coba lagi.")

if __name__ == '__main__':
    main()

