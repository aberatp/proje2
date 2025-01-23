# Tablo 5 oluşturulması
import pandas as pd

relation_data_path = 'Tablo_1.xlsx'
student_success_path = 'Tablo_4_Student_2_______1.xlsx'

relation_data = pd.read_excel(relation_data_path)
student_success_data = pd.read_excel(student_success_path)

relation_values = relation_data["İlişki Değeri"]
program_outcomes = relation_data["Prg Çıktı"]

success_percentages = student_success_data.iloc[:, 1:-2]
average_success = success_percentages.mean(axis=1)

program_success = []
for i, prg_outcome in enumerate(program_outcomes):
    relation_value = relation_values[i]
    if relation_value > 0:
        success_ratio = average_success[i] / relation_value
    else:
        success_ratio = 0
    program_success.append(success_ratio)

output_df = pd.DataFrame({
    "Prg Çıktı": program_outcomes,
    "Başarı Oranı": program_success
})

for i, column in enumerate(student_success_data.columns[1:-2]):
    output_df[column] = success_percentages.iloc[:, i]

output_path = 'Tablo_5.xlsx'
output_df.to_excel(output_path, index=False)

print(f"Tablo 5 '{output_path}' dosyasına kaydedildi.")