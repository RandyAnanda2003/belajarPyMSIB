#excersie 1
# nama = "randy aulia"
# umur = 21
# berat = 62
# print(f'halo nama saya {nama}. umur saya {umur}. dan berat badan saya {berat} kg')

#exercise 2
# def calc () :
#     num_1 = int(input("masukan bilangan pertama "))
#     num_2 = int(input("masukan bilangan kedua "))
#     penjumlahan = num_1+num_2
#     pengurangan = num_1-num_2
#     perkalian = num_1*num_2
#     pembagian = num_1/num_2
#     modulo = num_1%num_2
#     return penjumlahan,pengurangan,perkalian,pembagian,modulo
# print(calc())


#exercise 3
# nilai = float(input("masukan nilai yang akan diperiksa "))
# if nilai >= 90 : print ("A")
# elif nilai < 90 and nilai>=80 : print ("B")
# elif nilai <80 and nilai >=70 : print ("C")
# elif nilai <70 and nilai >=60 : print ("D")
# else : print("F")

#exercise 4 
# angka = int(input("masukan angka dengan "))
# # for i in range (1,angka+1 ) :
# #     print(i,end="")

# i=1
# while i<=angka :
#     print(i,end="")
#     i+=1
    
#exercise 5
# def factorial (num) :
#     if num == 0 : return 1
#     else : 
#         result = num * factorial(num-1)
#         return result

# print(factorial(5))

#exercise 6
# fruits = [] 
# for i in range(5) :
#     fruit = input (f"masukan buah ke {i+1} : ") 
#     while fruit in fruits :
#         print(f'{fruit} already exist, please input another fruit ')
#         fruit = input (f"masukan buah ke {i+1} : ") 
#         if fruit not in fruits :
#             break
#     fruits.append(fruit)
# print(fruits)

#exercise 7
# toko_buah = {
#     "Apel" : "20.000",
#     "jeruk" : "10.000"
# }

# for buah,harga in toko_buah.items() :
#     print(f'Nama : {buah}, Harga : {harga}')

#exercise 8 
# def is_even (num) :
#     if num%2 == 0 :
#         return True
#     else : return False
# print(is_even(5))

#exercise 9
# import math_operation_module as math
# print(math.penjumlah(num_1=4,num_2=2))
# print(math.pengurangan(num_1=4,num_2=2))
# print(math.perkalian(num_1=4,num_2=2))
# print(math.pembagian(num_1=4,num_2=2))

#exercise 10
# inventory = list(("Pisau", "peta", "kompas"))

# def findFruits() :
#     for i in range (3) :
#         fruit = input(f"masukan buah temuan ke- {i+1} : ")
#         while fruit in inventory :
#             fruit = input(f"{fruit} is already exist in inventory. please input another fruit: ")
#             if fruit not in inventory :
#                 break
#         inventory.append(fruit)
#     print(inventory)

# findFruits()

from petualangan_module import Player
player_1 = Player(keberanian=0, nama="", kekuatan=0)

def findFruits(player):  # Ubah parameter dari name menjadi player untuk lebih jelas
    for i in range(3):
        fruit = input(f"Masukan buah temuan ke-{i+1}: ")
        while fruit in player.inventory:  # Akses atribut inventory dari player (objek Player)
            fruit = input(f"{fruit} is already in inventory. Please input another fruit: ")
            if fruit not in player.inventory:
                break
        player.tambah_inventory(fruit)  # Panggil metode tambah_inventory untuk player
    print(player.inventory)
    player.tambah_element_rencana("makanan", 3)  # Gunakan player, bukan randy

def hadapiHewan(player):  # Ubah parameter menjadi player
    player.tambah_keberanian(int(input("seberapa berani kamu : ")))  
    if player.keberanian > 7:
        print("Kamu berhasil mengusir hewan buas!")
        player.tambah_inventory("taring hewan")
    else:
        player.kurangi_keberanian(2)
        print(player.keberanian) 

def sebrangiSungai (player) :
    player.ubahNama(input("siapa nama kamu sekarang ? : "))
    player.tambah_kekuatan(int(input("seberapa berani kamu ? : ")))
    if player.kekuatan > 5 : print(f'kamu berhasil menyebrangi sungai, {player.nama}')
    else : 
        print(f'kamu harus mencari jalan lain {player.nama}') 
        player.tambah_inventory("rakit")
        print(player.inventory)

def bukaPintu() :
    status = False
    while status==False :
        kode = int(input("masukan angka rahasia "))
        if 120%kode == 0 :
            print("kamu berhasil membuka pintu ! ")
            break
        else : print("angka yang dimasukan salah, coba lagi ! ")

def buatRencana(player):
    player.tambah_element_rencana("hari",3)
    player.tambah_element_rencana("barang_diperlukan",["kompas","peta","rakit"])
    print(player_1.rencana_pulang)


def cekInventaris(player) :
    if set(player_1.rencana_pulang["barang_diperlukan"]).issubset(set(player_1.inventory)):
        print ("Rencana Bisa dilaksanakan")
        return player.ubahStatus(True)
    else :
        print("kamu perlu mencari lebih banyak barang")

from petualangan_module import countScoreInventory as count

def akhirPetualangan (player) :
    if player.status_keberhasilan == True :
        print(f'Kamu Berhasil pulang dengan selamat !, petualangan mu berhasil dengan skor {count(player.inventory)}')
    else :
        print("kamu belum bisa pulang, tetaplah berusaha dan coba main lagi ya !")

# Panggil fungsi dengan objek 
findFruits(player_1)
hadapiHewan(player_1)
sebrangiSungai(player_1)
bukaPintu()
buatRencana(player_1)
cekInventaris(player_1)
akhirPetualangan(player_1)

