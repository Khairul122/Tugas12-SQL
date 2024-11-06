import pandas as pd
import matplotlib.pyplot as plt
from mysql.connector import connect

def create_connection():
    return connect(
        host='localhost',
        user='root',
        passwd='',
        database='pikm',
    )

query = """
SELECT m_kbli.kbli, COUNT(*) as jumlah 
FROM perusahaan
JOIN m_kbli ON perusahaan.kbli_id = m_kbli.id
WHERE perusahaan.kecamatan = 'KUALA'
GROUP BY m_kbli.kbli
"""

with create_connection() as koneksi:
    try:
        df = pd.read_sql(query, koneksi)
        print("\nData yang diambil:")
        print(df)

        if not df.empty:
            plt.figure(figsize=(20, 4))
            plt.pie(df['jumlah'], labels=df['kbli'], autopct='%1.1f%%')
            plt.title('Distribusi Jenis Industri di Kecamatan Kuala')
            plt.legend(df['kbli'], 
                      title="Jenis KBLI",
                      loc="center left",
                      bbox_to_anchor=(1, 0, 0.5, 1))
            
            plt.axis('equal')
            plt.tight_layout()
            plt.show()
            
            print("\nDistribusi Jenis Industri di Kecamatan Kuala:")
            print(df.to_string(index=False))
        else:
            print("\nTidak ada data yang ditemukan untuk kecamatan KUALA")

    except Exception as e:
        print(f"Error saat menjalankan query: {e}")