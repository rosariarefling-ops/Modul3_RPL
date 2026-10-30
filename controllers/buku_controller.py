# Rosaria Reflin Gala_029
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        # Menginisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        # Binding tombol perbarui, hapus, dan klik tabel
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)
        self.selected_id = None

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_update.configure(state="disabled")
            self.view.btn_delete.configure(state="disabled")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()
        
    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
            
        # Mengambil data dari Model (Database)
        data_buku = self.model.get_all_buku()
        
        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku["id_buku"], buku["judul"], buku["penulis"], buku["tahun_terbit"]))

# Rosaria Reflin Gala_029            
    def simpan_data(self):
        # Proteksi ganda di level Controller[cite: 18]
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return
        
        # Mengambil teks dari inputan di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        
        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
            
        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)
        
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            # Bersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            # Muat ulang tabel agar data baru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    # === TAMBAHAN UNTUK TUGAS ===
    def pilih_data_tabel(self, event):
     selected_item = self.view.tabel.selection()
     if selected_item:
         values = self.view.tabel.item(selected_item[0], "values")
         self.selected_id = values[0]
         self.view.entry_judul.delete(0, 'end')
         self.view.entry_judul.insert(0, values[1])
         self.view.entry_penulis.delete(0, 'end')
         self.view.entry_penulis.insert(0, values[2])
         self.view.entry_tahun.delete(0, 'end')
         self.view.entry_tahun.insert(0, values[3])

    def perbarui_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()
        berhasil = self.model.update_buku(self.selected_id, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.muat_data_tabel()

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?"):
            berhasil = self.model.delete_buku(self.selected_id)
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.muat_data_tabel()

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()

