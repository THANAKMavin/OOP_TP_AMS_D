print("===== Student Score Evaluation =====")

while 1>0:
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
        elif score >= 60:
            status = "Pass"
            grade = "D"
            print(f"Score: {score} | Status: {status} | Grade: {grade}")
        elif score >= 50:
            status = "Pass"
            grade = "E"
            print(f"Score: {score} | Status: {status} | Grade: {grade}")
        else:
            status = "Fail"
            grade = "F"
            print(f"Score: {score} | Status: {status} | Grade: {grade}")

    check_student_score()
print("\n\n")