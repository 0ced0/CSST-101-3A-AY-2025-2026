"""
Enhanced Mini Expert System: University Logic Rules
With CSV Logging for Record-Keeping
"""


import csv;
from datetime import datetime;

def impl(p, q):
        return (not p) or q 


def tf(b: bool) -> str:
        return "T" if b else "F"

def log_result(student_name, rule_name, result):
    with open("logic_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            student_name, rule_name, result])
        


def attendance_rule(student_name):
    print("\n ---Attendance Rule Checker---")
    late = input("Is the student late? (T/F): ").strip().upper() == "T"
    excuse = input("DId the student bring an excuse letter? (T/F): ").strip().upper() == "T"

    result = impl(late, excuse)
    outcome = "Satisfied /" if result else "Violated X"

    print(f"p = {tf(late)} (Late), q = {tf(excuse)} (Excuse Letter)")
    print("Result: ", outcome)

    log_result(student_name, "Attendance Rule", outcome)


def grading_rule(student_name):
    print("\n--- Grading Rule Checker ---")
    try:
        grade = float(input("Enter student grade: "))
    except ValueError:
            print("Invalid grade input.")
            return

    p = grade >= 75
    q = grade >= 75
    result = impl(p, q)
    outcome = "Saatisfied /" if result else "Violated X"

    print(f"P = {tf(p)} (grade >= 75), Q = {tf(q)} (student passes)")
    print("Result: ", outcome)

    log_result(student_name, "Grading Rule", outcome)


def login_rule(student_name):
    print("\n ---Login Checker ---")
    correct_password = "admin123"
    attempt = input("Enter password: ")

    p = (attempt == correct_password) 
    q = (attempt == correct_password)
    result = impl(p, q)
    outcome = "Accessgranted /" if result else "Acces denied X"

    print(f"P = {tf(p)} (Password Correct), Q = {tf(q)} (Access Granted)")
    print("Result: ", outcome)

    log_result(student_name, "Login Rule", outcome)



def bonus_rule(student_name):
    print("\n--- Bonus Points Eligibility Checker ---")
    regular = input("Does the student have regular attendance? (T/F): ")
    bonus = regular
    result = impl(regular, bonus)
    outcome = "Satisfied /" if result else "Violated X"

    print(f"P = {tf(regular)} (Regular Attendance), Q = {tf(bonus)} (Bonus Eligible)")
    print("Result: ", outcome)

    log_result(student_name, "Bonus Rule", outcome)


def main():
    print("=== University Logic Rules System ===")
    student_name = input("Enter student name: ").strip()

    while True:
        print("\n======================")
        print(" Main Menu ")
        print("\n======================")
        print("1) Attendance Rule Checker")
        print("2) Grading RUle Checker")
        print("3) Login System Rules Checker")
        print("4) Bonus POint Checker")
        print("5) Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
                attendance_rule(student_name)
        elif choice == "2":
                grading_rule(student_name)
        elif choice == "3":
                login_rule(student_name)
        elif choice == "4":
                bonus_rule(student_name)
        elif choice == "5":
                print("Exiting... Results saved to logic_results.csv")
                break
        else: 
                print("Invalid choice. Try again.")


if __name__=="__main__":
    with open("logic_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Student Name", "Rule", "Result"])
    
    main()