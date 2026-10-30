#Rosaria Reflin Gala_F5212510029
from controllers.buku_controller import BukuController
from controllers.anggota_controller import AnggotaController

if __name__ == "__main__":
    print("=== SISTEM MANAJEMEN PERPUSTAKAAN ===")
    print("1. Kelola Data Buku")
    print("2. Kelola Data Anggota")
    
    pilihan = input("Pilih aplikasi (1/2): ")
    
    if pilihan == "1":
        app = BukuController()
        app.run()
    elif pilihan == "2":
        app = AnggotaController()
        app.run()
    else:
        print("Pilihan tidak valid!")