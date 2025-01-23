# Tablo 1 oluşturulması
import pandas as pd
import numpy as np

file_path = "C:\\Users\\berat\\Downloads\\NotYukle-BLM315-2024-1-Random.xlsx"
df = pd.read_excel(file_path)

program_outcomes = [1, 2, 3, 4, 5]
lesson_outcomes = [1, 2, 3, 4, 5]

relation_matrix = np.random.choice([0, 0.2, 0.5, 0.8, 1], size=(len(program_outcomes), len(lesson_outcomes)))

relation_values = relation_matrix.mean(axis=1)

output_df = pd.DataFrame(relation_matrix, columns=[f"Ders Çıktısı {i}" for i in lesson_outcomes])
output_df.insert(0, "Prg Çıktı", program_outcomes)
output_df["İlişki Değeri"] = relation_values

output_path = 'Tablo_1.xlsx'
output_df.to_excel(output_path, index=False)

print(f"İlişki tablosu '{output_path}' dosyasına kaydedildi.")