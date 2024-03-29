stack = []

def tambah_barang(stack, barang_baru) :
    stack.append(barang_baru)
    print(f"{barang_baru} berhasil ditambahkan ke dalam stack.")
    
def hapus_barang_terakhir(stack) :
    if len(stack) == 0 :
        print("Stack kosong, tidak ada barang yang dapat di hapus.")
    else :
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} berhasil dihapus dalam stack.")
        
    def tampilkan_barang_teratas(stack):
        if len(stack) == 0 :
            print("Stack kosong, tidak ada barang yang dapat ditampilkan.")
        else : 
            barang_teratas = stack[-1]
            print(f"Barang teratas didalam stack adalah{barang_teratas}.")
            
    while True : 
        print("\nGudang saat ini : ", stack)
        print("Menu :")
        print("1. Tambah Barnag")
        print("2. Hapus Barang Terkahir")
        print("3. Tampilkan Barang Teratas")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
        if pilihan == "1":
            barang_baru = input("Masukkan nama barang yang akan ditambahkan :")
            tambah_barang(stack, barang_baru)
        elif pilihan == "2" :
            hapus_barang_terakhir(stack)
        elif pilihan == "3" :
            tampilkan_barang_teratas(stack)
        elif pilihan == "4" :
            print("Terima kasih telah menggunakan progmram ini.")
            break
        else : 
            print("Pilihan tidak valid. Silahkan masukkan pilihan yang benar.")