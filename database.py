class Data:
    def __init__(self):
        self.students = {}
        self.applications = {}
        self.admin_password = "secretadmin"
        self.allotments = {}

    def student_sign_up(self):
        name = input("Enter full name: ", type=TEXT)
        password = input("Enter password: ", type=PASSWORD)
        if name in self.students:
            put_error("Student already exists!")
        else:
            self.students[name] = password
            put_success("Student signed up successfully!")

    def check_pswd(self, name):
        password = input("Enter password: ", type=PASSWORD)
        if name in self.students and self.students[name] == password:
            return True
        else:
            return False

    def set_userinfo(self, user_type, name):
        self.current_user = {"type": user_type, "name": name}

    def get_vacancies(self):
        return {"CS": 10, "IT": 5, "ECE": 8}

    def view_seat_matrix(self):
        vacancies = self.get_vacancies()
        for branch, seats in vacancies.items():
            put_text(f"{branch}: {seats} seats available")

    def apply_for_seat(self):
        branch = input("Enter preferred branch (CS/IT/ECE): ", type=TEXT)
        name = self.current_user["name"]
        self.applications[name] = branch
        put_success(f"Application submitted for {branch} branch")

    def withdraw_application(self):
        name = self.current_user["name"]
        if name in self.applications:
            del self.applications[name]
            put_success("Application withdrawn")
        else:
            put_error("No application found to withdraw")

    def change_password(self):
        name = self.current_user["name"]
        new_password = input("Enter new password: ", type=PASSWORD)
        self.students[name] = new_password
        put_success("Password changed successfully")

    def admin_allot_seats(self):
        for name, branch in self.applications.items():
            if branch in self.allotments:
                self.allotments[branch].append(name)
            else:
                self.allotments[branch] = [name]
        put_success("Allotment process completed")

    def view_allotment_results(self):
        for branch, students in self.allotments.items():
            put_text(f"{branch} branch: {', '.join(students)}")

    def view_branch_allotment(self):
        branch = input("Enter branch (CS/IT/ECE): ", type=TEXT)
        if branch in self.allotments:
            put_text(f"{branch} branch: {', '.join(self.allotments[branch])}")
        else:
            put_text(f"No allotments found for {branch} branch")

    def search_student(self):
        name = input("Enter student name: ", type=TEXT)
        found = False
        for branch, students in self.allotments.items():
            if name in students:
                put_text(f"{name} allotted to {branch} branch")
                found = True
                break
        if not found:
            put_text("Student not found in any branch")
