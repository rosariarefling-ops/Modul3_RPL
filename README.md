# Sistem Manajemen Perpustakaan (MVC Python)

## Deskripsi Singkat Aplikasi
Aplikasi **Sistem Manajemen Perpustakaan** berbasis desktop ini dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan pola arsitektur **Model-View-Controller (MVC)**. Antarmuka (*UI*) pengguna dirancang menggunakan pustaka **CustomTkinter** untuk memberikan tampilan modern, serta terhubung ke basis data MySQL menggunakan `mysql-connector-python`. Sistem ini juga dilengkapi dengan fitur keamanan non-fungsional seperti autentikasi pengguna, enkripsi kata sandi *hash* SHA-256, pembatasan hak akses berbasis peran (*Role-Based Access Control* / RBAC), serta pengujian otomatis menggunakan `pytest` dan integrasi CI/CD melalui GitHub Actions.

---

## Struktur Direktori MVC
Proyek ini diorganisasikan ke dalam struktur direktori berikut:
- `config/` : Berisi konfigurasi koneksi utama ke basis data MySQL (`database.py`).
- `models/` : Berisi kelas logika data dan kueri basis data menggunakan *Parameterized Query* (`buku_model.py`, `user_model.py`).
- `views/`  : Berisi antarmuka grafis atau *user interface* berbasis CustomTkinter dan Tkinter (`login_view.py`, `buku_view.py`).
- `controllers/` : Berisi kelas pengendali yang menjembatani interaksi antara Model dan View, termasuk pengaturan alur *login* dan otorisasi hak akses tombol (`auth_controller.py`, `buku_controller.py`).
- `tests/`  : Berisi skrip pengujian unit otomatis (*unit testing*) menggunakan `pytest` (`test_auth.py`, `test_buku.py`).
- `.github/workflows/` : Berisi berkas konfigurasi *pipeline* otomatisasi CI (`ci_pipeline.yml`).

---

## Panduan Instalasi & Konfigurasi Database MySQL
Ikuti langkah-langkah berikut untuk menyiapkan lingkungan pengembangan di komputer lokal:

1. **Persiapan Database:**
   - Pastikan aplikasi **Laragon** sudah diinstal dan layanan **MySQL** dalam keadaan aktif.
   - Buka terminal MySQL, lalu buat basis data baru dengan perintah:
     ```sql
     CREATE DATABASE perpustakaan;
     ```

2. **Kloning & Virtual Environment:**
   - Buka direktori proyek Anda melalui Visual Studio Code.
   - Aktifkan *virtual environment* (`env`) di terminal:
     ```bash
     ./env/Scripts/activate
     ```

3. **Instalasi Dependensi:**
   - Pasang seluruh pustaka yang dibutuhkan menggunakan berkas `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

---

## Cara Menjalankan Aplikasi
1. Pastikan layanan database MySQL di Laragon menyala.
2. Pastikan *virtual environment* (`env`) aktif di terminal VS Code.
3. Jalankan titik masuk utama (*entry point*) aplikasi dengan perintah:
   python main.py
4. Jendela **Login Sistem** akan muncul. Masukkan kredensial akun uji coba berikut untuk masuk:
   - **Akun Admin:** `petugas` | *Password:* `admin123`
   - **Akun Anggota:** `mahasiswa` | *Password:* `user123`