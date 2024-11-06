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
SELECT *
FROM perusahaan
WHERE (jenisproduk = 'INDUSTRI AIR MINUM DAN AIR MINERAL'
  OR komoditi = 'AIR MINUM')
  AND kecamatan = 'KUALA';
"""

df = pd.read_sql_query(query, conn)

conn.close()

industry_counts = df.groupby('kecamatan').size().reset_index(name='jumlah_industri')

industry_counts = industry_counts.sort_values(by="jumlah_industri", ascending=False)

industry_counts['cumulative_percentage'] = industry_counts['jumlah_industri'].cumsum() / industry_counts['jumlah_industri'].sum() * 100

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(industry_counts['kecamatan'], industry_counts['jumlah_industri'], color='skyblue')
ax.set_xlabel('Kecamatan')
ax.set_ylabel('Jumlah Industri', color='b')
ax.set_title('Pareto Chart of Industri Air Minum di Kecamatan Kuala')

ax2 = ax.twinx()
ax2.plot(industry_counts['kecamatan'], industry_counts['cumulative_percentage'], 
        color='red', marker="D", linestyle='-', linewidth=2)
ax2.set_ylabel('Cumulative Percentage (%)', color='r')
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}%'))

plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()