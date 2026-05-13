from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser, GpaAnalyser


fm = FileManager("students.csv")
fm.check_file()
fm.create_output_folder("output")

dl = DataLoader("students.csv")
dl.load()
dl.preview()

analysers = [
    TopStudentsAnalyser(dl.students),
    GpaAnalyser(dl.students),
]

print("-" * 30)
print("Running all analysers:")
print("-" * 30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()
    print()

main_analyser = analysers[0]
saver = ResultSaver(main_analyser.result, "output/result.json")
report = Report(main_analyser, saver)
report.generate()
