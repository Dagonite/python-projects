"""6. Create a class called ”Lecturer”. The lecturer class will need to hold the 
following information: first name, last name, salary, and units they teach. All
this information will be set at the point that the object is created
__init__(self ,first_name, last_name, salary, units_taught) - where units_taught
is a list. The university needs to be able to:

add new units add_unit(self, unit_name);
remove units which are no longer taught remove_unit(self, unit_name);
give the lecturer a pay rise give_pay_rise(self, rise_percentage);
print information they have about the lecturer print_lecturer_information(self).
"""


class Lecturer:
    def __init__(self, first_name, last_name, salary, units_taught):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.units_taught = units_taught
        pass

    def add_unit(self, unit_name):
        self.units_taught.append(unit_name)

    def remove_unit(self, unit_name):
        self.units_taught.remove(unit_name)

    def give_pay_rise(self, rise_percentage):
        self.salary *= 1 + (rise_percentage / 100)

    def print_lecturer_information(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Salary: £{self.salary:,.2f}\n"
            f"Units taught: {self.units_taught}\n"
        )


lecturer1 = Lecturer(
    "John", "Doe", 70000, ["Robotics", "Databases", "Machine learning"]
)
lecturer1.add_unit("Network security")
lecturer1.remove_unit("Databases")
lecturer1.give_pay_rise(5)
print(lecturer1.print_lecturer_information())
