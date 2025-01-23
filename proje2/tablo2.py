# Tablo 2 oluşturulması
import pandas as pd
import numpy as np

lesson_outcomes = [1, 2, 3, 4, 5]
evaluation_criteria = ["Öd1", "Öd2", "Quiz", "Vize", "Fin"]
criteria_weights = [10, 10, 10, 30, 40]

relation_matrix = np.random.choice([0, 1], size=(len(lesson_outcomes), len(evaluation_criteria)))

output_df = pd.DataFrame(relation_matrix, columns=evaluation_criteria)
output_df.insert(0, "Ders Çıktı", lesson_outcomes)

weights_df = pd.DataFrame([criteria_weights], columns=evaluation_criteria)
weights_df.insert(0, "Ders Çıktı", ["Ağırlıklar"])

final_df = pd.concat([weights_df, output_df], ignore_index=True)

output_path = 'Tablo_2.xlsx'
final_df.to_excel(output_path, index=False)

print(f"Tablo 2 '{output_path}' dosyasına kaydedildi.")