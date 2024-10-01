class Player : 
    def __init__(self,keberanian,nama,kekuatan) :
       self.nama = nama
       self.inventory = ["pisau,","peta","kompas"]
       self.keberanian = keberanian
       self.kekuatan = kekuatan
       self.rencana_pulang = {}
       self.status_keberhasilan = False
    
    def ubahNama (self, p_nama) :
        self.nama =p_nama
    
    def ubahStatus (self,update_status) :
        self.status_keberhasilan = update_status

    def tambah_kekuatan (self,penambahan) :
        self.kekuatan += penambahan

    def tambah_inventory (self,barang) :
        self.inventory.append(barang)
    
    def tambah_keberanian (self,penambahan) :
        self.keberanian += penambahan
    
    def kurangi_keberanian (self,pengurangan) :
        self.keberanian -= pengurangan

    def habiskan_element_rencana (self, key_rencana) :
        if key_rencana in self.rencana_pulang :
            while self.rencana_pulang[key_rencana] > 0 : 
                print(f"makanan sisa {self.rencana_pulang[key_rencana]}")
                self.rencana_pulang[key_rencana]-= -1

    def tambah_element_rencana (self, key_rencana, val_key_rencana) :
        if key_rencana in self.rencana_pulang :
            self.rencana_pulang[key_rencana]+=val_key_rencana
        else :
            self.rencana_pulang[key_rencana] = val_key_rencana



def countScoreInventory(inventory_list) :
    sum_score = 0
    buku_nilai = {
    "pisau" : 10,
    "kompas" : 20,
    "rakit" : 30,
    "pisang" : 2,
    "anggur" : 8,
    "kurma" : 5
    }
    for barang in inventory_list :
        if barang in buku_nilai :
            sum_score += buku_nilai[barang]

    return sum_score

    