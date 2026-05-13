import csv

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.students = []

    def load(self):
        try:
            with open(self.filepath, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Загружено студентов: {len(self.students)}")
        except FileNotFoundError:
            print(f"Ошибка: файл {self.filepath} не найден.")
            self.students = []
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            self.students = []

    def preview(self, n=3):
        print(f"\n--- Первые {n} записи ---")
        for row in self.students[:n]:
            print(row)
        print("---\n")
