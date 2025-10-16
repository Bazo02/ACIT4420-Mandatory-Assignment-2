from students import Students
import json

class StudentsManager:
    """Class to manage student data with JSON storage, using Students class."""

    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students = Students()
        self.load_students()

    def load_students(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for s in data:
                    self.students.add_student(
                        s['name'],
                        s['email'],
                        s['course'],
                        s['preferred_time']
                    )
        except FileNotFoundError:
            pass

    def save_students(self):
        with open(self.file_path, "w") as file:
            json.dump(self.students.get_students(), file, indent=4)

    def add_student(self, name, email, course, preferred_time="08:00"):
        self.students.add_student(name, email, course, preferred_time)
        self.save_students()

    def remove_student(self, email):
        self.students.remove_student(email)  
        self.save_students()

    def get_students(self):
        return self.students.get_students()
