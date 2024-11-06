import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pikm"
)

companies = ["MENJAHIT SURYATI", "USAHA PERABOT", "USAHA BORDIR"]

query = """
SELECT perusahaan, nilaiinvestasi, nilaiproduksi 
FROM perusahaan
WHERE perusahaan IN (%s, %s, %s)
"""

df = pd.read_sql_query(query, conn, params=companies)

conn.close()

plt.figure(figsize=(12, 8))

colors = ['#FF6347', '#4682B4', '#32CD32']  
markers = ['o', 's', 'D']  

for i, company in enumerate(companies):
    company_data = df[df['perusahaan'] == company]
    plt.scatter(
        company_data['nilaiinvestasi'], 
        company_data['nilaiproduksi'], 
        color=colors[i], 
        marker=markers[i], 
        s=100,  
        label=company  
    )

plt.xlabel("Nilai Investasi", fontsize=14)
plt.ylabel("Nilai Produksi", fontsize=14)
plt.title("Perbandingan Nilai Investasi vs Nilai Produksi", fontsize=16)
plt.legend(title="Perusahaan", fontsize=12)

for i, txt in enumerate(df['perusahaan']):
    plt.annotate(
        txt, 
        (df['nilaiinvestasi'].iloc[i], df['nilaiproduksi'].iloc[i]),
        textcoords="offset points",
        xytext=(5, 5),
        ha='center',
        fontsize=10,
        color='darkblue'
    )

plt.grid(True, linestyle='--', alpha=0.7)  
plt.tight_layout()
plt.show()
