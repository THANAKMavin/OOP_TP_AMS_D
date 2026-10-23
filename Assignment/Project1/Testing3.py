def evaluate_student(score):
    if score < 0 or score > 100:
        return "Invalid score! Please enter a value between 0 and 100."

    if score >= 90:
        status = "Pass"
        grade = "A"
    elif score >= 80:
        status = "Pass"
        grade = "B"
    elif score >= 70:
        status = "Pass"
        grade = "C"
    elif score >= 50:
        status = "Pass"
        grade = "D"
    else:
        status = "Fail"
        grade = "F"
    return f"Score: {score} | Status: {status} | Grade: {grade}"

print(evaluate_student(96))
print(evaluate_student(85))
print(evaluate_student(45))
print(evaluate_student(199))


def check_student_score():
    student_input = input("Enter your score: ")
    score = int(student_input)

    if score < 0 or score > 100:
        print("Invalid score! Please enter number between 0 to 100.")
    elif score >= 90:
        status = "Pass"
        grade = "A"
        print(f"Score: {score} | Status: {status} | Grade: {grade}")
    elif score >= 80:
        status = "Pass"
        grade = "B"
        print(f"Score: {score} | Status: {status} | Grade: {grade}")
    elif score >=70:
        status = "Pass"
        grade = "C"
        print(f"Score: {score} | Status: {status} | Grade: {grade}")
    elif score >= 50:
        status = "Pass"
        grade = "D"
        print(f"Score: {score} | Status: {status} | Grade: {grade}")
    else:
        status = "Fail"
        grade = "F"
        print(f"Score: {score} | Status: {status} | Grade: {grade}")

check_student_score()