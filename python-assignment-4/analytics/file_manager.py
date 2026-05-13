import os

class FileManager:
    def __init__(self, filepath):
        self.filepath = filepath  # путь к CSV-файлу

    def check_file(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Файл не найден: {self.filepath}")
        print(f"Файл найден: {self.filepath}")

    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Папка создана: {folder}/")
        else:
            print(f"Папка уже существует: {folder}/")
