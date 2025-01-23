# Tablo 3 oluşturulması
import pandas as pd

file_path = 'Tablo_2.xlsx'
relation_data = pd.read_excel(file_path)

weights = relation_data.iloc[0, 1:].astype(float) / 100

relation_data = relation_data.iloc[1:].reset_index(drop=True)

weighted_matrix = relation_data.iloc[:, 1:] * weights

weighted_matrix["TOPLAM"] = weighted_matrix.sum(axis=1)

weighted_matrix.insert(0, "Ders Çıktı", relation_data["Ders Çıktı"])

output_path = 'Tablo_3.xlsx'
weighted_matrix.to_excel(output_path, index=False)

print(f"Ağırlıklı Değerlendirme Tablosu '{output_path}' olarak kaydedildi.")