import json
import os


NUM_STUDENTS = 1000
SUBJECTS = ["math", "science", "history", "english", "geography"]
DIRECTORY = r"C:/Users/Kacper/Desktop/PYTHON/Programming_Expert/Projects/student_performance/students"


def load_report_card(directory, student_number):
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(directory, f"{student_number}.json")
    path = os.path.join(base_path, file_path)

    try:
        with open(path, "r") as file:
            report_card = json.load(file)
    except FileNotFoundError:
        return {}

    return report_card

def average_student_mark():

    global SUBJECTS

    counter = {"num_of_students" : 0, "all_students_sum" : 0}

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        student_grade_sum = 0
        
        for subject in SUBJECTS:
            student_grade_sum += report_card[subject]
        
        student_average = student_grade_sum/len(SUBJECTS)

        counter["num_of_students"] += 1
        counter['all_students_sum'] += student_average
    
    average_student_mark = round(counter["all_students_sum"]/counter["num_of_students"], 2)

    print(f"Average Student Grade: {average_student_mark}")

def hardest_subject():
    global SUBJECTS
    global NUM_STUDENTS

    subjects_averages = dict.fromkeys(SUBJECTS)
    for subject in SUBJECTS:
        subjects_averages[subject] = 0

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        for subject in SUBJECTS:
            subjects_averages[subject] += report_card[subject]

    hardest_subject = min(subjects_averages, key=subjects_averages.get)

    print(f"Hardest Subject: {hardest_subject}")

def easiest_subject():
    global SUBJECTS
    global NUM_STUDENTS

    subjects_averages = dict.fromkeys(SUBJECTS)
    for subject in SUBJECTS:
        subjects_averages[subject] = 0

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        for subject in SUBJECTS:
            subjects_averages[subject] += report_card[subject]

    easiest_subject = max(subjects_averages, key=subjects_averages.get)

    print(f"Easiest Subject: {easiest_subject}")

def best_performing_grade():

    global SUBJECTS
    global NUM_STUDENTS

    GRADES_COUNTER = []

    for grade in range(8):
        GRADES_COUNTER.append({"grade":grade+1, "student_count":0, "mark_sum":0})

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        student_sum = 0

        for subject in SUBJECTS:
            student_sum += report_card[subject]

        student_average = student_sum/len(SUBJECTS)
        student_grade = report_card["grade"]

        index_of_grade = next((i for i, item in enumerate(GRADES_COUNTER) if item["grade"] == report_card["grade"]), None)

        GRADES_COUNTER[index_of_grade]["student_count"] += 1
        GRADES_COUNTER[index_of_grade]["mark_sum"] += student_average

    best_grade = max(GRADES_COUNTER, key = lambda d: d["mark_sum"])["grade"]

    print(f"Best Performing Grade: {best_grade}")

def worst_performing_grade():

    global SUBJECTS
    global NUM_STUDENTS

    GRADES_COUNTER = []

    for grade in range(8):
        GRADES_COUNTER.append({"grade":grade+1, "student_count":0, "mark_sum":0})

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        student_sum = 0

        for subject in SUBJECTS:
            student_sum += report_card[subject]

        student_average = student_sum/len(SUBJECTS)
        student_grade = report_card["grade"]

        index_of_grade = next((i for i, item in enumerate(GRADES_COUNTER) if item["grade"] == report_card["grade"]), None)

        GRADES_COUNTER[index_of_grade]["student_count"] += 1
        GRADES_COUNTER[index_of_grade]["mark_sum"] += student_average

    worst_grade = min(GRADES_COUNTER, key = lambda d: d["mark_sum"])["grade"]

    print(f"Worst Performing Grade: {worst_grade}")

def best_student():

    global SUBJECTS
    global NUM_STUDENTS

    best_student = None

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        student_sum = 0

        for subject in SUBJECTS:
            student_sum += report_card[subject]

        student_average = student_sum/len(SUBJECTS)
        report_card.update({"average":student_average})

        if best_student == None:
            best_student = report_card
        else:
            if student_average > best_student['average']:
                best_student = report_card
            else:
                continue
    
    print(f"Best Student ID: {best_student['id']}")

def worst_student():

    global SUBJECTS
    global NUM_STUDENTS

    worst_student = None

    for student_number in range(NUM_STUDENTS):
        report_card = load_report_card(DIRECTORY, student_number)

        student_sum = 0

        for subject in SUBJECTS:
            student_sum += report_card[subject]

        student_average = student_sum/len(SUBJECTS)
        report_card.update({"average":student_average})

        if worst_student == None:
            worst_student = report_card
        else:
            if student_average < worst_student['average']:
                worst_student = report_card
            else:
                continue
    
    print(f"Worst Student ID: {worst_student['id']}")


average_student_mark()
hardest_subject()
easiest_subject()
best_performing_grade()
worst_performing_grade()
best_student()
worst_student()

