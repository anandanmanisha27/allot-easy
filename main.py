from database import *
import time
from pywebio.input import *
from pywebio.output import *
from allotment_mechanism import *

mydata = Data()  # object of class Data
mymachine = Allotment_mechanism()
welm_img = open('images/Welcome to AllotEasy.jpg', 'rb').read()  
header_img = open('images/header_new.jpg', 'rb').read()
aboutus_img = open('images/Aboutus_img.jpg', 'rb').read()

class Menu:
    def __init__(self): 
        self.user = None

    def about_us(self):
        clear('ROOT')  
        with use_scope("main", clear=True):
            put_image(aboutus_img, width='150%', height='400px')
            data = input_group("Press button to return to menu", [
                actions('', [{'label': 'Back', 'value': 1}], name='action', help_text=None),
            ])
        clear('ROOT')

    def login(self):
        with use_scope("main", clear=True):
            put_image(src=welm_img, width='150%', height='400px')
        login_choice = input_group('Get Started', [
            actions('', [ 
                {'label': 'Sign Up', 'value': 1}, 
                {'label': 'Login (Student)', 'value': 2}, 
                {'label': 'Login (Admin)', 'value': 3}, 
                {'label': 'About Us', 'value': "Aboutus"},
                {'label': 'Exit', 'value': 4}, 
            ], name='action', help_text=None),
        ])
        
        user_inp = login_choice["action"]
        if user_inp == "Aboutus":
            self.user = None
            clear("main")
            self.about_us()
            return
        else:    
            self.user = user_inp
            if user_inp == 1:
                clear("main")
                mydata.student_sign_up()
            if user_inp == 2:
                name_surname = input("Enter full name (name surname): ", type=TEXT, required=True)
                name = (name_surname.split())[0]
                mydata.set_userinfo(2, name)
                is_correct_pswd = mydata.check_pswd(name)
                if is_correct_pswd:
                    with use_scope("main"):
                        put_success(f"\n Welcome, {name.capitalize()}!")
                    time.sleep(2)
                    self.menu_for_student()
                    return
                else:
                    with use_scope("main"):
                        put_error("Sorry! Incorrect credentials.", closable=True)
                    time.sleep(2)
                    self.login()
            if user_inp == 3:
                pwd = input("Enter password:", type=PASSWORD, required=True)
                if pwd == "secretadmin":
                    with use_scope("main"):
                        put_success("Welcome, Admin!")
                    mydata.set_userinfo(3, "admin")
                    time.sleep(2)
                    self.menu_for_admin()
                else:
                    with use_scope("main"):
                        put_error("Sorry! Incorrect password entered.", closable=True)
                    time.sleep(2)
                    self.login()

    def menu_for_student(self):
        choice = None
        while choice != 8:
            if mydata.flag == 0:
                data = input_group("Student Menu", [
                    radio(label="", name='menu', options=[
                        ("View Seat Matrix", 1),
                        ("Fill Application details", 2),
                        ("Check your application status", 3),
                        ("Withdraw application", 4),
                        ("View Branchwise cutoff marks", 5),
                        ("View data of vacancies left", 6),
                        ("Change Password", 7),
                        ("Logout", 8)
                    ], required=True, inline=False, value=None)
                ])
                choice = data['menu']
            else:
                choice = 8
            if choice != 8:
                clear("main")
                if choice == 1:
                    mydata.view_seat_matrix()
                if choice == 2:
                    mydata.apply_for_seat()
                if choice == 3:
                    put_text("Application status functionality to be implemented")
                if choice == 4:
                    mydata.withdraw_application()
                if choice == 5:
                    put_text("Branchwise cutoff marks functionality to be implemented")
                if choice == 6:
                    put_text(mydata.get_vacancies())
                if choice == 7:
                    mydata.change_password()
        return

    def menu_for_admin(self):
        clear('ROOT') 
        choice = None 
        while choice != 7:  
            if mymachine.flag == 0:
                data = input_group("Admin Menu", [
                    radio(label="", name='menu', options=[
                        ("Run Seat allotment process", 1),
                        ("View full allotment result", 2),
                        ("View branch-wise allotment result", 3),
                        ("Search a student", 4),
                        ("Get list of students without allotment", 5),
                        ("View data of vacancies left", 6),
                        ("Logout", 7)
                    ], required=True, inline=False, value=None)
                ])
                choice = data['menu']
            else:
                choice = 7
            if choice != 7:
                clear()
                if choice == 1:
                    mymachine.run_allotment()
                    mydata.admin_allot_seats()
                if choice == 2:
                    mydata.view_allotment_results()
                if choice == 3:
                    mydata.view_branch_allotment()
                if choice == 4:
                    mydata.search_student()
                if choice == 5:
                    put_text("List of students without allotment functionality to be implemented")
                if choice == 6:
                    put_text(mydata.get_vacancies())

if __name__ == '__main__':
    menu = Menu()
    menu.login()
