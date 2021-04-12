# Student List


class Student:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.programme = None

    def set_first_name(self, fname):
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_programme(self, prog):
        if prog in ["BMI", "BMS"]:
            self.programme = prog
        else:
            raise ValueError("Programme can only be 'BMI' or 'BMS'")

    def print_data(self):
        print("Student's name is " + self.first_name + " " +
              self.last_name + ", undergraduate programme is " + self.programme)

# example
student1 = Student()
student1.set_first_name("John")
student1.set_last_name("Wick")
student1.set_programme("BMS")
student1.print_data()