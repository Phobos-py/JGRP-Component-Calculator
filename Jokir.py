#Ultimate JGRP optimized with def(function)

import os 
import math 

# important element
depo = 0
history_list = []
HEADER_KALKULATOR = "Kalkulator penghitung compo CUAN-101JK"
MINCOMPO = 500
TARIF_RENDAH = 0.65 # <- jika compo yang dibutuhkan banyak
TARIF_TINGGI = 0.75 # <- jika compo yang dibutuhkan sedikit
BATAS_PENENTU_TARIF = 150

#kumpulan function
def header():
    '''fungsi header'''
    os.system("cls")
    print(HEADER_KALKULATOR)
    print("Berikut list command yang tersedia : \n(1) Deposit \n(2) kalkulator \n(3) Check storage dan history \n(4) Exit")

def deposit():
    '''fungsi tambah deposit'''
    global depo
    depo_tambah = int(input("\nMasukan jumlah component yang ingin dideposit: "))
    depo += depo_tambah

def lanjut():
    '''fungsi melanjutkan'''
    lanjutkan = input("Ingin kembali ke menu? y/n: ").lower()

    if lanjutkan == "y" :
        return True
    else :
        return False

def input_component() :
    '''fungsi input kalkulator'''
    print(4*"<>" + "Kalkulator penghitung compo CUAN-101JK\n")

    compo_1 = int(input("Masukan jumlah component yang dibutuhkan (1) : "))

    print("Note: isi dengan (0) jika tidak diperlukan")

    compo_2 = int(input("Masukan jumlah component yang dibutuhkan (2) : "))
    compo_3 = 0

    if compo_2 > 0 :
        print("Note: isi dengan (0) jika tidak diperlukan")
        compo_3 = int(input("Masukan jumlah component yang dibutuhkan (3) : "))
    
    return compo_1, compo_2, compo_3
     

while True:
    header()

    command = input("silahkan pilih command (1/2/3/4) : ")
    
    if command == "4":
        break

    elif command == "1":
        deposit()
        print(f"Jumlah total depomu saat ini: {depo}")

        if not lanjut() :
            break
    
    elif command == "2" :
        if depo < MINCOMPO :
            print("Jumlah compo mulai habis disarankan mengisi ulang deposit")
            deposit()

        else :
            print(HEADER_KALKULATOR)

            compo_1, compo_2, compo_3 = input_component()
            jumlah_component = compo_1 + compo_2 + compo_3

            if jumlah_component < BATAS_PENENTU_TARIF :
                hasil = jumlah_component * TARIF_TINGGI

            elif jumlah_component > BATAS_PENENTU_TARIF :
                hasil = jumlah_component * TARIF_RENDAH

            modal_uang = jumlah_component * 0.55
            int_1 = math.floor(hasil)
            int_2 = math.floor(modal_uang)
            profit = int_1 - int_2
            print("\n", 4*"<>" + "Hasilnya\n")

            print(f"Jumlah component       : {jumlah_component}")
            print(f"biaya untuk memperbiki : {modal_uang} $")
            print(f"Harga untuk pelanggan  : {hasil} $")
            print(f"Profit yang didapat : {profit} $")
            print("Silahkan bernegoisasi dengan pelanggan sampai harga cocok\n")

            if not lanjut() :
                break

    elif command == "3" :
        
        hasil_depo = depo - jumlah_component

        new_history = [depo,"-",jumlah_component,"=",hasil_depo]
        history_list.append(new_history)

        depo = depo - jumlah_component
        print(f"\nJumlah component anda saat ini : {depo} Component\n")

        print("="*5, "History", "="*5)
        for index,history in enumerate(history_list) :
            print(f"{index+1} {history[0]} {history[1]} {history[2]} {history[3]} {history[4]}\n")
        
        if not lanjut() :
            break

print("Kalkulator dihentikan, Terima kasih")
input("Tekan Enter untuk keluar...")