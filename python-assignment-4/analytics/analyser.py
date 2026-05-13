class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        valid = list(
            filter(lambda s: s.get("GPA") not in ("", None, "GPA"), self.students)
        )

        try:
            sorted_students = sorted(
                valid,
                key=lambda s: float(s["GPA"]),
                reverse=True
            )
        except (ValueError, KeyError) as e:
            print(f"Ошибка сортировки: {e}")
            sorted_students = []

        top = sorted_students[:10]

        self.result = {
            "total_students": len(self.students),
            "top_10": [
                {
                    "student_id": s.get("student_id", "N/A"),
                    "GPA": float(s["GPA"]),
                    "final_exam_score": float(s.get("final_exam_score", 0)),
                    "country": s.get("country", "N/A"),
                }
                for s in top
            ],
        }

    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)

        print(f"total_students: {self.result.get('total_students', 0)}")
        print("top_10:")
        for i, student in enumerate(self.result.get("top_10", []), 1):
            print(
                f"  #{i:2d}  id={student['student_id']}  "
                f"GPA={student['GPA']:.2f}  "
                f"exam={student['final_exam_score']:.0f}  "
                f"country={student['country']}"
            )
        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top Students by GPA, {len(self.students)} students"



class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        valid = list(
            filter(lambda s: s.get("GPA") not in ("", None, "GPA"), self.students)
        )
        try:
            gpas = list(map(lambda s: float(s["GPA"]), valid))
        except (ValueError, KeyError):
            gpas = []

        if not gpas:
            self.result = {}
            return

        high = list(filter(lambda g: g > 3.5, gpas))

        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(gpas) / len(gpas), 2),
            "max_gpa": max(gpas),
            "min_gpa": min(gpas),
            "high_performers": len(high),
        }

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"
