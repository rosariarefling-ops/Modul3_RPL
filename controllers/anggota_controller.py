import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()
        
        # Binding tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        
        # Penanganan variabel tombol update
        if hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(command=self.perbarui_data)
        elif hasattr(self.view, 'btn_perbarui'):
            self.view.btn_perbarui.configure(command=self.perbarui_data)

        # Penanganan variabel tombol delete
        if hasattr(self.view, 'btn_delete'):
            self.view.btn_delete.configure(command=self.hapus_data)
        elif hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)

        # Binding klik baris tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)
        
        self.selected_id = None
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota["id_anggota"], anggota["nama"], anggota["alamat"]))

    def pilih_data_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            values = self.view.tabel.item(selected_item[0], "values")
            self.selected_id = values[0]
            self.view.entry_nama.delete(0, 'end')
            self.view.entry_nama.insert(0, values[1])
            self.view.entry_alamat.delete(0, 'end')
            self.view.entry_alamat.insert(0, values[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return
        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()

    def perbarui_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()
        berhasil = self.model.update_anggota(self.selected_id, nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu!")
            return
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?"):
            berhasil = self.model.delete_anggota(self.selected_id)
            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()

    def bersihkan_form(self):
        self.selected_id = None
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def run(self):
        self.view.mainloop()
        