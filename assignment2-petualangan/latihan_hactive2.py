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

