from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()

    def get_all_anggota(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM anggota")
        return cursor.fetchall()

    def create_anggota(self, nama, alamat):
        cursor = self.conn.cursor()
        query = "INSERT INTO anggota (nama, alamat) VALUES (%s, %s)"
        cursor.execute(query, (nama, alamat))
        self.conn.commit()
        return True

    def update_anggota(self, id_anggota, nama, alamat):
        cursor = self.conn.cursor()
        query = "UPDATE anggota SET nama = %s, alamat = %s WHERE id_anggota = %s"
        cursor.execute(query, (nama, alamat, id_anggota))
        self.conn.commit()
        return True

    def delete_anggota(self, id_anggota):
        cursor = self.conn.cursor()
        query = "DELETE FROM anggota WHERE id_anggota = %s"
        cursor.execute(query, (id_anggota,))
        self.conn.commit()
        return True