# Rosaria Reflin Gala_029
from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()
    
    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor
    
    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)
    
    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

# === TAMBAHAN UNTUK TUGAS 3 ===
def test_get_all_buku_berhasil():
    model = BukuModel()
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_cursor.fetchall.return_value = [
        {"id_buku": 1, "judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "tahun_terbit": 2005}
    ]
    model.conn.cursor.return_value = mock_cursor
    
    hasil = model.get_all_buku()
    
    assert isinstance(hasil, list)
    assert len(hasil) == 1
    assert hasil[0]["judul"] == "Laskar Pelangi"
    mock_cursor.execute.assert_called_once()
    