import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="pikm"
)

query = """
SELECT komoditi, SUM(nilaiinvestasi) as total_investasi 
FROM perusahaan 
WHERE kecamatan = 'KUALA' 
AND komoditi IN ('PANGAN', 'PERABOT', 'SANDANG', 'KOSEN', 'KETAMPANG', 
                'BORDIR', 'ALAT PERTANIAN', 'USAHA GARAM', 'AIR MINUM', 
                'BENGKEL RODA 2', 'PENGETAMAN KAYU', 'MENJAHIT')
GROUP BY komoditi
ORDER BY total_investasi DESC
"""

df = pd.read_sql(query, conn)

df['percentage'] = df['total_investasi'] / df['total_investasi'].sum() * 100
df['cumulative_percentage'] = df['percentage'].cumsum()

plt.figure(figsize=(12, 6))

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.bar(df['komoditi'], df['total_investasi'], color='skyblue')

ax2.plot(df['komoditi'], df['cumulative_percentage'], color='red', marker='o', linewidth=2)

plt.title('Diagram Pareto Nilai Investasi per Komoditi di Kecamatan KUALA', pad=20)
ax1.set_xlabel('Komoditi')
ax1.set_ylabel('Nilai Investasi (Rp)')
ax2.set_ylabel('Persentase Kumulatif (%)')

plt.xticks(rotation=45, ha='right')

ax1.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()

conn.close()