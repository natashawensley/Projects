class Student:
    def __init__(self, name, age, phone_number, form_class, subjects, gender, enrollment_status):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.gender = gender
        self.enrolment_status = enrollment_status

    def display_info(self, name, age, phone_number, form_class, subjects, gender, enrollment_status):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.form_class = form_class
        self.subjects = subjects
        self.gender = gender
        self.enrolment_status = enrollment_status

def generate_students():
    import csv
    with open('random_students.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter='|')
        for line in filereader:
            if line [5] == "True":
                is_male = True
            else:
                is_male = False
            Student(line[0], int(line[1]), line[2], line[3], line[4], is_male)


        def find_student():
            searched_student = input("Which student would you  like  to search for: ")
            for x in range len(student_list):
                if searched_student == student_list[]:
                    print_student_details()

def print_student_details():
    for student in display_info:
        display.display_info()

def select_student_age():
    if student.age > int(input("What age of student would you think to search for")):
        display_info()


# Main routine
Student("Karen", "17", "123-4567", "WNLR", "13DTC", "13SMX", "Female")
Student("Bob", "18", "021-0263674", "BNNL", "13MX", "Male")
Student("Lisa", "16", "022-4567123", "SKWR", "13DTC", "13SMX", "Female")
Student("Patrick", "18", "023-01234556", "SCBE", "13ENG", "13CMX", "13DTC", "Male")

student_list = []
generate_students()
