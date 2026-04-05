# ============================================
# STEP 1: IMPORT LIBRARIES
# ============================================

import json


# ============================================
# STEP 2: USER INPUT FUNCTIONS
# ============================================

def get_user_info():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            break
        print("Please enter only letters!")

    while True:
        surname = input("Enter your surname: ")
        if surname.isalpha():
            break
        print("Surname must contain only letters!")

    while True:
        student_id = input("Enter your student ID (digits only): ")
        if student_id.isdigit():
            break
        print("Only digits!")

    dob = input("Enter your date of birth Ex:(YYYY-MM-DD): ")

    return name, surname, student_id, dob


# ============================================
# STEP 3: FILE HANDLING FUNCTIONS
# ============================================

def save_results(data):
    choice = input("Do you want to save your results? (yes/no): ").lower()

    if choice == "yes":
        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Results saved successfully!")


def load_results():
    try:
        with open("results.json", "r") as file:
            data = json.load(file)
            print("\n - Previous Results -")
            for key, value in data.items():
                print(f"{key}: {value}")
    except FileNotFoundError:
        print("No saved results found.")


# ============================================
# STEP 4: QUESTIONNAIRE DATA & LOGIC
# ============================================

def run_questionnaire():

    # ---- QUESTION LIST ----
    list_of_questions = [
    "1)It is easy to stay focused during lectures: ",
    "2)I can concentrate on academic tasks for more than 30 minutes without distraction: ",
    "3)External noises do not affect my concentration in class: ",
    "4)I can easily return to focusing after being distracted: ",
    "5)I follow the teacher’s explanations without losing attention: ",
    "6)I am able to avoid distractions from my phone while studying: ",
    "7)I can stay focused even during long explanations: ",
    "8)I remember important details from lectures: ",
    "9)I rarely feel mentally tired during lessons: ",
    "10)I complete study tasks without switching to other activities: ",
    "11)I feel calm and focused while studying: ",
    "12)I can maintain concentration even during boring lessons: ",
    "13)I manage my time well without getting distracted: ",
    "14)I stay focused even when I feel tired: ",
    "15)I can ignore irrelevant thoughts while studying: ",
    "16)I maintain attention throughout the entire lecture: ",
    "17)I am able to complete assignments without losing focus: ",
    "18)I stay engaged during classroom activities: ",
    "19)I can control my attention during study sessions: ",
    "20)Overall, my concentration during academic tasks is strong: "
    ]

    # ---- INITIAL SCORE ----
    score = 0

    # ---- INSTRUCTIONS ----
    print('''Sustained Attention and Classroom Concentration Assessment

Strongly Disagree = 0
Disagree = 1
Neutral = 2
Agree = 3
Strongly Agree = 4
''')

    # ---- QUESTION LOOP ----
    for i in list_of_questions:
        while True:
            try:
                answer = int(input(i))
                if 0 <= answer <= 4:
                    score = answer + score
                    break
                else:
                    print("Enter a number between 0 and 4.")
            except ValueError:
                print("Invalid input! Enter numbers only.")

    # ---- OUTPUT SCORE ----
    print(f"""Your total score is:
          {score}""")

    # ---- CLASSIFICATION ----
    if score <= 16:
        result = "Excellent sustained attention"
    elif score <= 32:
        result = "Good concentration"
    elif score <= 48:
        result = "Moderate attention"
    elif score <= 64:
        result = "Low concentration"
    else:
        result = "Very poor concentration"

    print("Result:", result)

    return score, result


# ============================================
# STEP 5: MAIN MENU SYSTEM
# ============================================

while True:
    print("\n - MENU -")
    print("1. Start new questionnaire")
    print("2. Load previous results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name, surname, student_id, dob = get_user_info()
        score, result = run_questionnaire()

        data = {
            "name": name,
            "surname": surname,
            "student_id": student_id,
            "dob": dob,
            "score": score,
            "result": result
        }

        save_results(data)

    elif choice == "2":
        load_results()

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid option. Try again.")