# SAKSHI'S OFFICIAL CSCA MATH & PHYSICS PREPARATION ENGINE
# An authentic tracker to log self-study progress for the January 2027 sitting

def main():
    # Initializing clean candidate tracking variables
    student_name = "Sakshi"
    python_study_minutes = 0
    csca_math_hours = 0
    csca_physics_hours = 0
    completed_milestones = []

    print(f"CSCA Target Tracking Engine Activated for Candidate: {student_name}")
    print("System configured for the Mathematics & Physics dual-track sitting.\n")

    while True:
        print("--- CSCA PREPARATION COMMAND MENU ---")
        print("1. Log Python Programming Self-Study Minutes")
        print("2. Log CSCA Mathematics Preparation Hours")
        print("3. Log CSCA Physics Preparation Hours")
        print("4. Append Verified Syllabus Milestone")
        print("5. Render Live Performance Dashboard")
        print("6. Exit System")
        
        choice = input("Select operation option (1-6): ").strip()

        if choice == '1':
            user_input = input("Enter self-study coding runtime (Minutes): ").strip()
            minutes = int(user_input)
            if minutes > 0:
                python_study_minutes = python_study_minutes + minutes
                print(f"[SUCCESS] Added {minutes} minutes to Python Applied Logic Account.")
            else:
                print("[ERROR] Value input must be a positive integer.")

        elif choice == '2':
            user_input = input("Enter hours spent on CSCA Math modules today: ").strip()
            hours = float(user_input)
            if hours > 0:
                csca_math_hours = csca_math_hours + hours
                print(f"[SUCCESS] Logged {hours} structural preparation hours to Math Account.")
            else:
                print("[ERROR] Value input must be a positive number.")

        elif choice == '3':
            user_input = input("Enter hours spent on CSCA Physics modules today: ").strip()
            hours = float(user_input)
            if hours > 0:
                csca_physics_hours = csca_physics_hours + hours
                print(f"[SUCCESS] Logged {hours} analytical preparation hours to Physics Account.")
            else:
                print("[ERROR] Value input must be a positive number.")

        elif choice == '4':
            milestone = input("Describe achieved syllabus module/mock target: ").strip()
            if milestone:
                completed_milestones.append(milestone)
                print(f"[SUCCESS] Permanent Milestone Locked: '{milestone}'")
            else:
                print("[ERROR] Objective parameter string cannot be blank.")

        elif choice == '5':
            # Rendering a clean layout designed for university review boards
            print("\n" + "="*55)
            print(f"        CSCA STANDARDIZED ASSESSMENT PORTFOLIO       ")
            print(f"        Candidate Identifier: {student_name.upper()}      ")
            print("="*55)
            print(f" [✓] Applied Computational Analytics (Python) : {python_study_minutes} Mins")
            print(f" [✓] STEM Framework Tracker (Mathematics)     : {csca_math_hours} Hours")
            print(f" [✓] STEM Framework Tracker (Physics)         : {csca_physics_hours} Hours")
            print("\n Verified Target Advancements for January Intake:")
            
            if len(completed_milestones) == 0:
                print("     [!] Array Null: No verified milestones uploaded for this sitting.")
            else:
                counter = 1
                for milestone in completed_milestones:
                    print(f"     [{counter}] {milestone}")
                    counter = counter + 1
            print("="*55)

        elif choice == '6':
            print("Terminating tracking window. Maintain strict focus on Math & Physics!")
            break

        else:
            print("[INVALID ENTRY] Operational parameter out of bounds. Select 1-6.")

if __name__ == "__main__":
    main()
