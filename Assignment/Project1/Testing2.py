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
    elif score >= 60:
        status = "Pass"
        grade = "D"
    elif score >= 50:
        status = "Pass"
        grade = "E"
    else:
        status = "Fail"
        grade = "F"
    return f"Score: {score} | Status: {status} | Grade: {grade}"

print(evaluate_student(96))
print(evaluate_student(85))
print(evaluate_student(45))
print(evaluate_student(55))
print(evaluate_student(199))
