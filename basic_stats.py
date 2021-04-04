import statistics


class Student:

    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade


def basic_stats(obj):
    all_grades = []

    for items in range(len(obj)):
        all_grades.append(obj[items].get_grade())

    mean_grades = statistics.mean(all_grades)
    median_grades = statistics.median(all_grades)
    mode_grades = statistics.mode(all_grades)

    grades_tuple = (mean_grades, median_grades, mode_grades)

    return grades_tuple

