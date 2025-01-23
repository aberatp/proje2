# Tablo 4 oluşturulması
import pandas as pd

student_scores_path = 'C:\\Users\\berat\\Downloads\\NotYukle-BLM315-2024-1-Random.xlsx'
weighted_evaluation_path = 'Tablo_3.xlsx'

student_scores = pd.read_excel(student_scores_path)
weighted_evaluation = pd.read_excel(weighted_evaluation_path)

weighted_evaluation_columns = ["Ders Çıktı"] + list(student_scores.columns[1:6]) + ["TOPLAM"]
weighted_evaluation.columns = weighted_evaluation_columns

student_results = {}
for i, row in student_scores.iterrows():
    student_no = row["Ogrenci_No"]
    student_performance = weighted_evaluation.iloc[:, 1:-1].multiply(row[1:], axis=1)
    student_performance["TOPLAM"] = student_performance.sum(axis=1)
    student_performance["MAX"] = weighted_evaluation["TOPLAM"] * 100
    student_performance["%Başarı"] = (student_performance["TOPLAM"] / student_performance["MAX"]) * 100
    student_performance.insert(0, "Ders Çıktı", weighted_evaluation["Ders Çıktı"])
    student_results[student_no] = student_performance

for student_no, result in student_results.items():
    valid_student_no = str(student_no).replace("*", "_")
    output_path = f'Tablo_4_Student_{valid_student_no}.xlsx'
    result.to_excel(output_path, index=False)
    print(f"{student_no} için Tablo 4 başarıyla oluşturuldu ve {output_path} olarak kaydedildi.")