import json
import os

class ResultSaver:
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def save_json(self):
        try:
            folder = os.path.dirname(self.filepath)
            if folder and not os.path.exists(folder):
                os.makedirs(folder)

            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.result, f, ensure_ascii=False, indent=2)
            print(f"Result saved to {self.filepath}")
        except IOError as e:
            print(f"Ошибка при сохранении файла: {e}")
