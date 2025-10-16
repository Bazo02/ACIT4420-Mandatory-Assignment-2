# main.py
from students_manager import StudentsManager
from reminder_sender import send_reminder
from logger import log_reminder
from scheduler import schedule_reminders
from reminder_generator import generate_reminder
import re

def manual_trigger(students_manager: StudentsManager):
    """Send reminders immediately to all students."""
    students = students_manager.get_students()
    if not students:
        print("No students found.")
        return

    print("Manual trigger: sending reminders now...\n")
    for s in students:
        reminder = generate_reminder(s['name'], s['course'])
        send_reminder(s.get('email', ''), reminder)
        log_reminder(s, reminder)
    print("\nDone.\n")

def list_students(students_manager: StudentsManager):
    """Print all students."""
    students = students_manager.get_students()
    if not students:
        print("No students found.")
        return
    print("\nCurrent students:")
    for s in students:
        print(f"- {s['name']} | {s['email']} | {s['course']} | {s['preferred_time']}")
    print()

def add_student_flow(students_manager: StudentsManager):
    """Interactive flow to add a student."""
    print("\nAdd a new student")

    # Name
    while True:
        name = input("Name: ").strip()
        if not name:
            print("Name is required!")
        else:
            break

    # Email
    while True:
        email = input("Email: ").strip()
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            print("A valid email is required!")
        else:
            break

    # Course
    while True:
        course = input("Course: ").strip()
        if not course:
            print("Course is required!")
        else:
            break

    # Preferred time
    while True:
        preferred_time = input("Preferred time (e.g., 08:00): ").strip().replace('.', ':')
        if not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", preferred_time):
            print("Preferred time must be in HH:MM format (24-hour clock)!")
        else:
            break

    students_manager.add_student(name, email, course, preferred_time)
    print(f"Student '{name}' added.")

def remove_student_flow(students_manager: StudentsManager):
    """Interactive flow to remove a student."""
    print("\nRemove a student")

    # List students
    students = students_manager.get_students()
    if not students:
        print("No students found.")
        return

    print("Select a student to remove:")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']} | {s['email']} | {s['course']} | {s['preferred_time']}")
    
    # Select student
    while True:
        try:
            choice = int(input("Enter the student number to remove: ")) - 1
            if choice < 0 or choice >= len(students):
                raise ValueError
            student_to_remove = students[choice]
            break
        except ValueError:
            print("Invalid choice. Please enter a number from the list.")

    # Confirm removal
    confirm = input(f"Are you sure you want to remove '{student_to_remove['name']}'? (y/n): ").strip().lower()
    if confirm == 'y':
        students_manager.remove_student(student_to_remove['email'])
        print(f"Student '{student_to_remove['name']}' removed.")
    else:
        print("Removal canceled.")

def main():
    students_manager = StudentsManager()
    while True:
        print("1. List students")
        print("2. Add student")
        print("3. Remove student")
        print("4. Send reminders now")
        print("5. Start scheduler")
        print("6. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            list_students(students_manager)
        elif choice == "2":
            add_student_flow(students_manager)
        elif choice == "3":
            remove_student_flow(students_manager)
        elif choice == "4":
            manual_trigger(students_manager)
        elif choice == "5":
            print("Starting scheduler (Ctrl+C to stop)...")
            schedule_reminders(
                students_manager,
                generate_reminder,
                send_reminder,
                log_reminder
            )
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
