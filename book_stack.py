stack=[]

def tambah_buku(stack, buku_baru):
    stack.append(buku_baru) 
    print(f"{buku_baru} berhasil ditambahkan ke dalam stack.")

def hapus_buku_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada buku yang dapat dihapus.") 
    else:
        buku_terakhir=stack.pop()
        print(f"{buku_terakhir} berhasil dihapus dari stack.")

def tampilkan_buku_teratas(stack):
    if len(stack)==0: 
        print("Stack kosong, tidak ada buku yang dapat ditampilkan.")
    else:
        buku_teratas=stack[-1]
        print(f"buku teratas di dalam stack adalah {buku_teratas}.")

while True:
    print("\nGudang saat ini:",stack)
    print("Menu:")
    print("1.Tambah Buku")
    print("2.Hapus BukuTerakhir")
    print("3.Tampilkan Buku Teratas")
    print("4.Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4):")
    if pilihan=="1":
        buku_baru=input("Masukkan nama buku yang akan ditambahkan: ")
        tambah_buku(stack, buku_baru)
    elif pilihan=="2":
        hapus_buku_terakhir(stack)
    elif pilihan=="3":
        tampilkan_buku_teratas(stack)
    elif pilihan=="4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        