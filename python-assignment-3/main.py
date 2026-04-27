import os
import csv
import json


# Task 1 — Class FileManager

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")



# Task 2 — Class DataLoader

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("-" * 30)



# Task 3 — Class DataAnalyser

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        # Sort students by final_exam_score descending
        sorted_students = sorted(
            self.students,
            key=lambda x: float(x['final_exam_score']),
            reverse=True
        )
        top10 = sorted_students[:10]

        top10_list = []
        for i, s in enumerate(top10, start=1):
            try:
                top10_list.append({
                    "rank": i,
                    "student_id": s['student_id'],
                    "country": s['country'],
                    "major": s['major'],
                    "final_exam_score": float(s['final_exam_score']),
                    "GPA": float(s['GPA'])
                })
            except ValueError:
                print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
                continue

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top10_list
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)
        for s in self.result.get("top_10", []):
            print(f"{s['rank']}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        print("-" * 30)

        print("=" * 30)
        print("ANALYSIS RESULT")
        print("=" * 30)
        print(f"Analysis       : Top 10 Students by Exam Score")
        print(f"Total students : {self.result['total_students']}")
        print("Top 10 saved to output/result.json")
        print("=" * 30)


# Task 4 — Class ResultSaver

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")



# Lambda / Map / Filter

def run_lambda_filter(students):
    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)

    top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, students))
    print(f"final_exam_score > 95  : {len(top_scorers)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"GPA values (first 5)   : {gpa_values[:5]}")

    good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, students))
    print(f"assignment_score > 90  : {len(good_assignments)}")

    print("-" * 30)



# Task 5 — Main

def main():
    # FileManager
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    # DataLoader
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    # DataAnalyser
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    # Lambda / Map / Filter
    run_lambda_filter(dl.students)

    # Exception handling test
    test_loader = DataLoader('students.csv')
    test_loader.load()

    wrong_loader = DataLoader('wrong_file.csv')
    wrong_loader.load()

    # ResultSaver
    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()


if __name__ == '__main__':
    main()